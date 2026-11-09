#!/usr/bin/env python3
"""
Hebrew Legal Terminology Lookup Tool

Standalone script that provides quick lookup of Hebrew legal terms,
their English translations, and context for Israeli legal research.

Usage:
    python legal_term_lookup.py
    python legal_term_lookup.py --term "bagatz"
    python legal_term_lookup.py --term "סעיף"
    python legal_term_lookup.py --list
    python legal_term_lookup.py --area employment
"""

from __future__ import annotations

import argparse
import sys

# Comprehensive Hebrew legal terminology database
LEGAL_TERMS = {
    # Court system
    "bagatz": {
        "hebrew": "בג\"ץ (בית משפט גבוה לצדק)",
        "english": "High Court of Justice",
        "context": "Supreme Court sitting as High Court of Justice. Hears petitions against government actions.",
        "area": "courts",
    },
    "beit mishpat elyon": {
        "hebrew": "בית המשפט העליון",
        "english": "Supreme Court",
        "context": "Highest court in Israel. Sits as appellate court and as High Court of Justice (Bagatz).",
        "area": "courts",
    },
    "beit mishpat mechozi": {
        "hebrew": "בית משפט מחוזי",
        "english": "District Court",
        "context": "Mid-level court. 6 districts. Handles serious criminal and high-value civil cases at first instance, and appeals from the Magistrate Court.",
        "area": "courts",
    },
    "beit mishpat shalom": {
        "hebrew": "בית משפט שלום",
        "english": "Magistrate Court",
        "context": "Lower court. Handles less serious criminal cases and civil claims up to a monetary threshold (Courts Law s.51). Family matters go to a Magistrate Court designated to sit as a Family Court (Family Courts Law s.2).",
        "area": "courts",
    },
    "beit mishpat lemishpacha": {
        "hebrew": "בית המשפט לענייני משפחה",
        "english": "Family Court",
        "context": "A Magistrate Court designated by order to hear family matters (Family Courts Law 1995 s.2).",
        "area": "courts",
    },
    "beit mishpat leinyanim minhaliyim": {
        "hebrew": "בית משפט לעניינים מינהליים",
        "english": "Administrative Court",
        "context": "The District Court sitting to hear petitions, appeals and claims listed in the Administrative Courts Law 2000 Schedules (s.5).",
        "area": "courts",
    },
    "beit din laavoda": {
        "hebrew": "בית דין לעבודה",
        "english": "Labor Court",
        "context": "Specialized court for employment disputes. Regional and national levels.",
        "area": "courts",
    },
    "beit din rabani": {
        "hebrew": "בית דין רבני",
        "english": "Rabbinical Court",
        "context": "Religious court with jurisdiction over Jewish marriage and divorce.",
        "area": "courts",
    },

    # Legislation types
    "chok": {
        "hebrew": "חוק",
        "english": "Law / Statute",
        "context": "Primary legislation enacted by the Knesset.",
        "area": "legislation",
    },
    "chok yesod": {
        "hebrew": "חוק יסוד",
        "english": "Basic Law",
        "context": "Quasi-constitutional law with higher normative status. A regular law may still infringe a protected right if it meets the limitation clause (e.g. Basic Law: Human Dignity and Liberty s.8), and Basic Law: Freedom of Occupation s.8 allows an express override by an absolute-majority law. Only some Basic Laws are entrenched.",
        "area": "legislation",
    },
    "pkuda": {
        "hebrew": "פקודה",
        "english": "Ordinance",
        "context": "Pre-state legislation (British Mandate era) still in force. Examples: Torts Ordinance, Income Tax Ordinance.",
        "area": "legislation",
    },
    "takana": {
        "hebrew": "תקנה",
        "english": "Regulation",
        "context": "Secondary legislation enacted by a minister under authority granted by a chok.",
        "area": "legislation",
    },
    "tzav": {
        "hebrew": "צו",
        "english": "Order",
        "context": "Administrative order, often used for extending laws or setting rates.",
        "area": "legislation",
    },
    "saif": {
        "hebrew": "סעיף",
        "english": "Section",
        "context": "A section of a law. Example: Saif 12 of Contracts Law.",
        "area": "legislation",
    },
    "saif katan": {
        "hebrew": "סעיף קטן",
        "english": "Subsection",
        "context": "A subsection within a section of a law.",
        "area": "legislation",
    },
    "tikun": {
        "hebrew": "תיקון",
        "english": "Amendment",
        "context": "An amendment to an existing law. Numbered sequentially.",
        "area": "legislation",
    },

    # Legal proceedings
    "tvia": {
        "hebrew": "תביעה",
        "english": "Claim / Lawsuit",
        "context": "Filing a legal action in court.",
        "area": "procedure",
    },
    "ktav tvia": {
        "hebrew": "כתב תביעה",
        "english": "Statement of Claim",
        "context": "The opening document filed by the plaintiff (tovea) in a civil case.",
        "area": "procedure",
    },
    "ktav hagana": {
        "hebrew": "כתב הגנה",
        "english": "Statement of Defense",
        "context": "The defendant's (nitba) response to the statement of claim.",
        "area": "procedure",
    },
    "erur": {
        "hebrew": "ערעור",
        "english": "Appeal",
        "context": "Appeal of a court decision to a higher court.",
        "area": "procedure",
    },
    "psak din": {
        "hebrew": "פסק דין",
        "english": "Judgment / Court Ruling",
        "context": "The court's final decision in a case. Under Basic Law: The Judiciary s.20, a Supreme Court holding (halacha) binds all courts except the Supreme Court itself; a lower court's holding only guides courts below it.",
        "area": "procedure",
    },
    "hachlata": {
        "hebrew": "החלטה",
        "english": "Decision / Order",
        "context": "Interim court decision during proceedings (not final judgment).",
        "area": "procedure",
    },
    "bakasha": {
        "hebrew": "בקשה",
        "english": "Motion / Application",
        "context": "A request filed with the court during proceedings.",
        "area": "procedure",
    },
    "tzav meni'a": {
        "hebrew": "צו מניעה",
        "english": "Injunction",
        "context": "Court order preventing a party from taking a specific action.",
        "area": "procedure",
    },

    "atira": {
        "hebrew": "עתירה",
        "english": "Petition",
        "context": "Proceeding against a public authority: to the Administrative Court for matters in the Administrative Courts Law First Schedule; some matters go to other courts or tribunals; the HCJ hears what no other court or tribunal has jurisdiction over (Basic Law: The Judiciary s.15(c)).",
        "area": "procedure",
    },
    "saad": {
        "hebrew": "סעד",
        "english": "Remedy / Relief",
        "context": "What a party asks the court to grant, e.g. damages, enforcement, a declaration, or an injunction.",
        "area": "procedure",
    },
    "tatzhir": {
        "hebrew": "תצהיר",
        "english": "Affidavit",
        "context": "A written statement of facts made under warning or oath, used as evidence in court proceedings.",
        "area": "procedure",
    },
    "netel haraaya": {
        "hebrew": "נטל הראיה",
        "english": "Burden of Proof",
        "context": "Which party must prove a fact. In civil cases the general standard is the balance of probabilities.",
        "area": "procedure",
    },
    "maazan hahistabruyot": {
        "hebrew": "מאזן ההסתברויות",
        "english": "Balance of Probabilities",
        "context": "The usual standard of proof in civil cases: more likely than not.",
        "area": "procedure",
    },
    "erur bezchut": {
        "hebrew": "ערעור בזכות",
        "english": "Appeal as of Right",
        "context": "An appeal that needs no permission, e.g. from a Magistrate Court judgment to the District Court (Courts Law s.52(a)).",
        "area": "procedure",
    },
    "tvia ktana": {
        "hebrew": "תביעה קטנה",
        "english": "Small Claim",
        "context": "Civil claim by an individual in the Small Claims Court, up to an index-linked ceiling (Courts Law s.60). A lawyer may appear only with the court's leave (s.63); appeal only by leave (s.64).",
        "area": "procedure",
    },
    "reshut erur": {
        "hebrew": "רשות ערעור (רע\"א)",
        "english": "Leave to Appeal",
        "context": "Permission needed to appeal certain decisions, e.g. an interim decision of a Magistrate Court or a District Court ruling given on appeal (Courts Law ss.41, 52).",
        "area": "procedure",
    },
    "diyun nosaf": {
        "hebrew": "דיון נוסף",
        "english": "Further Hearing",
        "context": "A rehearing of a Supreme Court judgment by an expanded panel. Check for one before treating a Supreme Court holding as settled.",
        "area": "procedure",
    },
    "halacha psuka": {
        "hebrew": "הלכה פסוקה",
        "english": "Binding Holding / Precedent",
        "context": "The legal rule a judgment decides, as opposed to obiter. Basic Law: The Judiciary s.20.",
        "area": "procedure",
    },

    # Legal professionals
    "orech din": {
        "hebrew": "עורך דין",
        "english": "Attorney / Lawyer",
        "context": "Licensed legal practitioner. Member of Israel Bar Association (Lishkat Orchei HaDin).",
        "area": "professionals",
    },
    "shofet": {
        "hebrew": "שופט",
        "english": "Judge",
        "context": "Appointed by President on recommendation of Judicial Selection Committee.",
        "area": "professionals",
    },
    "prakelit": {
        "hebrew": "פרקליט",
        "english": "Prosecutor / Advocate",
        "context": "State prosecutor (Praklitut HaMedina) or private advocate.",
        "area": "professionals",
    },
    "notar": {
        "hebrew": "נוטריון",
        "english": "Notary",
        "context": "Public notary for authentication of documents, especially for international use.",
        "area": "professionals",
    },

    # Contract law
    "choze": {
        "hebrew": "חוזה",
        "english": "Contract",
        "context": "A binding agreement between parties. Governed by Contracts Law (General Part) 1973.",
        "area": "contract",
    },
    "hatzaa": {
        "hebrew": "הצעה",
        "english": "Offer",
        "context": "A proposal to enter into a contract. Must show intent to contract and be definite enough to form one on acceptance; it may be addressed to the public (Contracts Law s.2).",
        "area": "contract",
    },
    "kibul": {
        "hebrew": "קיבול",
        "english": "Acceptance",
        "context": "Agreement to the terms of an offer, forming a binding contract.",
        "area": "contract",
    },
    "tom lev": {
        "hebrew": "תום לב",
        "english": "Good Faith",
        "context": "Fundamental principle in Israeli contract law. Required in negotiations, performance, and enforcement.",
        "area": "contract",
    },
    "hafarat choze": {
        "hebrew": "הפרת חוזה",
        "english": "Breach of Contract",
        "context": "Failure to perform contractual obligations. Remedies: enforcement, cancellation, damages.",
        "area": "contract",
    },

    # Employment law
    "piturin": {
        "hebrew": "פיטורין",
        "english": "Dismissal / Termination",
        "context": "Termination of employment by employer. Requires notice period and usually severance.",
        "area": "employment",
    },
    "pitzuei piturin": {
        "hebrew": "פיצויי פיטורין",
        "english": "Severance Pay",
        "context": "Severance Pay Law 1963 s.12(a): one month's salary per year for a salaried (monthly) employee; the statute states two weeks per year for a wage (hourly/daily) employee, which regulations under s.12(b) may raise. Check the current rule before stating a figure.",
        "area": "employment",
    },
    "hoda'a mukdemet": {
        "hebrew": "הודעה מוקדמת",
        "english": "Prior Notice",
        "context": "Required notice period before termination. Varies by seniority and pay type.",
        "area": "employment",
    },
    "schar minimum": {
        "hebrew": "שכר מינימום",
        "english": "Minimum Wage",
        "context": "Set by Minimum Wage Law 1987 and updated by government orders.",
        "area": "employment",
    },
    "chufsha shnatit": {
        "hebrew": "חופשה שנתית",
        "english": "Annual Leave / Vacation",
        "context": "Governed by Annual Leave Law 1951. Minimum days increase with seniority.",
        "area": "employment",
    },

    # Property law
    "zikat hanaa": {
        "hebrew": "זיקת הנאה",
        "english": "Easement",
        "context": "A charge on land for another's benefit without a right to possess it (Land Law s.5). A right of way (zchut ma'avar) is one kind.",
        "area": "property",
    },
    "tkufat bedek": {
        "hebrew": "תקופת בדק",
        "english": "Defect-Liability (Inspection) Period",
        "context": "Period after handover of a new apartment during which the developer must repair defects; length depends on the defect type (Sale (Apartments) Law 1973, s.4 and Schedule).",
        "area": "property",
    },
    "baalut": {
        "hebrew": "בעלות",
        "english": "Ownership",
        "context": "Full ownership rights over property. Registered in Tabu (Land Registry).",
        "area": "property",
    },
    "tabu": {
        "hebrew": "טאבו",
        "english": "Land Registry",
        "context": "Official land registration office. For settled land (mekarkein musdarim), registration is conclusive evidence of its contents; for unsettled land it is prima facie evidence only (Land Law s.125).",
        "area": "property",
    },
    "dira": {
        "hebrew": "דירה",
        "english": "Apartment",
        "context": "Residential unit. Defects in a new apartment sold by its developer: Sale (Apartments) Law 1973. Protection of buyer payments: Sale (Apartments) (Assurance of Investments) Law 1974.",
        "area": "property",
    },
}

# Legislation areas for filtering
AREAS = {
    "courts": "Court System",
    "legislation": "Legislation Types",
    "procedure": "Legal Proceedings",
    "professionals": "Legal Professionals",
    "contract": "Contract Law",
    "employment": "Employment Law",
    "property": "Property Law",
}


def _norm(text: str) -> str:
    """Fold case and Hebrew punctuation variants (gershayim, geresh, quotes)."""
    text = text.lower().strip()
    for ch in ('"', "'", "\u05f4", "\u05f3", "\u201c", "\u201d", "\u2019"):
        text = text.replace(ch, "")
    return " ".join(text.split())


def lookup_term(term: str) -> dict | None:
    """Look up a legal term by transliteration, English, or Hebrew."""
    term_lower = _norm(term)
    if not term_lower:
        return None
    # Exact match on the transliterated key (normalized, so "tzav meni'a" matches)
    for k, v in LEGAL_TERMS.items():
        if _norm(k) == term_lower:
            return v
    # Exact match on the Hebrew term (before any parenthetical expansion)
    for v in LEGAL_TERMS.values():
        if _norm(v["hebrew"].split("(")[0]) == term_lower:
            return v
    # Partial match on key, English, or Hebrew
    matches = {
        k: v for k, v in LEGAL_TERMS.items()
        if term_lower in _norm(k) or term_lower in v["english"].lower() or term_lower in _norm(v["hebrew"])
    }
    if len(matches) == 1:
        return next(iter(matches.values()))
    if matches:
        return {"multiple_matches": matches}
    return None


def list_all_terms():
    """Print all terms organized by area."""
    for area_key, area_name in AREAS.items():
        terms = {k: v for k, v in LEGAL_TERMS.items() if v["area"] == area_key}
        if terms:
            print(f"\n{'=' * 50}")
            print(f"  {area_name}")
            print(f"{'=' * 50}")
            for term_key, term_data in sorted(terms.items()):
                print(f"  {term_key:<25} {term_data['english']}")
                print(f"  {'':25} {term_data['hebrew']}")
                print()


def list_by_area(area: str):
    """Print terms for a specific area of law."""
    area_lower = area.lower().strip()
    if area_lower not in AREAS:
        print(f"Unknown area: {area}")
        print(f"Available areas: {', '.join(AREAS.keys())}")
        return False
    terms = {k: v for k, v in LEGAL_TERMS.items() if v["area"] == area_lower}
    print(f"\n{'=' * 50}")
    print(f"  {AREAS[area_lower]}")
    print(f"{'=' * 50}")
    for term_key, term_data in sorted(terms.items()):
        print(f"\n  Term: {term_key}")
        print(f"  Hebrew: {term_data['hebrew']}")
        print(f"  English: {term_data['english']}")
        print(f"  Context: {term_data['context']}")
    return True


def interactive_mode():
    """Run interactive lookup mode."""
    print("=" * 50)
    print("  Hebrew Legal Terminology Lookup")
    print("=" * 50)
    print()
    print("DISCLAIMER: For legal information only.")
    print("Consult a licensed attorney for legal advice.")
    print()
    print("Commands: type a term, 'list', 'area <name>', or 'quit'")
    print()

    while True:
        try:
            query = input("Lookup> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not query:
            continue
        if query.lower() == "quit":
            break
        if query.lower() == "list":
            list_all_terms()
            continue
        if query.lower().startswith("area "):
            list_by_area(query[5:])
            continue

        result = lookup_term(query)
        if result is None:
            print(f"  Term not found: {query}")
            print("  Try 'list' to see all available terms.")
        elif "multiple_matches" in result:
            print(f"  Multiple matches for '{query}':")
            for k in result["multiple_matches"]:
                print(f"    - {k}: {result['multiple_matches'][k]['english']}")
        else:
            print(f"\n  Term: {query}")
            print(f"  Hebrew: {result['hebrew']}")
            print(f"  English: {result['english']}")
            print(f"  Context: {result['context']}")
            print(f"  Area: {AREAS.get(result['area'], result['area'])}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Hebrew Legal Terminology Lookup Tool"
    )
    parser.add_argument("--term", "-t", help="Look up a specific term")
    parser.add_argument("--list", "-l", action="store_true", help="List all terms")
    parser.add_argument("--area", "-a", help="List terms by area of law")
    args = parser.parse_args()

    if args.list:
        list_all_terms()
    elif args.area:
        if not list_by_area(args.area):
            sys.exit(1)
    elif args.term is not None:
        result = lookup_term(args.term)
        if result is None:
            print(f"Term not found: {args.term}")
            sys.exit(1)
        elif "multiple_matches" in result:
            print(f"Multiple matches for '{args.term}':")
            for k, v in result["multiple_matches"].items():
                print(f"  {k}: {v['english']}, {v['context']}")
        else:
            print(f"Term: {args.term}")
            print(f"Hebrew: {result['hebrew']}")
            print(f"English: {result['english']}")
            print(f"Context: {result['context']}")
            print(f"Area: {AREAS.get(result['area'], result['area'])}")
    else:
        interactive_mode()


if __name__ == "__main__":
    main()

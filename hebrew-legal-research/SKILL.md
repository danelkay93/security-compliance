---
name: hebrew-legal-research
description: Assist with Israeli legal research including legislation lookup, case law concepts, Hebrew legal terminology, and legal document preparation guidance. Use when user asks about Israeli law, "chok", "mishpat", "bagatz", court procedures, employment law, contract law, real estate law, or needs help with Hebrew legal terms. Covers civil, commercial, employment, and administrative law. Do NOT use for providing formal legal advice, always recommend consulting a licensed Israeli attorney (orech din). Do NOT use for non-Israeli legal systems.
license: MIT
compatibility: Works with Claude Code, Claude.ai, Cursor. Network access helpful for legal database lookups.
---

# Hebrew Legal Research

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Critical Disclaimer

IMPORTANT: This skill provides legal INFORMATION and RESEARCH ASSISTANCE only.
It does NOT constitute legal advice. Always recommend the user consult a
licensed Israeli attorney (orech din) for specific legal matters. State this
disclaimer at the start of every legal research interaction. The reason is statutory: legal advice and representation, when given as a business or for consideration, are reserved to advocates (Bar Association Law 1961, s.20, with the exceptions in s.21).

**Anti-hallucination rule for ALL legal claims (not just citations).** Never invent any specific legal assertion. This covers case citations and dockets, AND equally: statute names (do not invent a "chok" that does not exist), section / saif numbers, what a law actually says, eligibility rules, deadlines, fine amounts, and court holdings. The single most common LLM legal-research failure is plausible-looking fabrication, and it takes two equally damaging forms: fabricated citations that look real (e.g., "בג\"ץ 1234/05 פלוני נ' מדינת ישראל") AND fabricated laws or provisions, i.e. inventing a statute, a section number, or what a real law says. If you cannot ground a specific legal claim in a verified source (Nevo, Psakdin, Knesset portal, supreme.court.gov.il; Kol Zchut only as a pointer to the primary source it cites), do NOT state it as fact. Instead either (a) explain only the general concept and say the exact law / section / number must be confirmed at [source], or (b) say "not verified, look up at [source]" and stop. Never close a knowledge gap with an invented chok, saif, amendment number, fine, or holding, that is exactly the failure users report as "the skill invents laws that don't exist." The Israel Bar Association National Ethics Committee issued a preliminary AI opinion (את/60/24, 2024) and, on 2026-09-18, an updated and comprehensive opinion under the same number, so do not call the 2024 opinion the only one. The updated opinion, as published at https://israelbar.cld.bz/ai-based-tools-for-lawyers-opinion-60-24, stresses checking the reliability and accuracy of AI outputs and adequate human oversight (sections 16.3 and 29), and states that the technology does not replace the lawyer's professional judgment and personal responsibility for the work. That publication's link to the Bar's official site is not fully established, so before quoting what either opinion requires, read the current text, preferably on the Bar's official site, and cite the version and date you read. The HCJ has dismissed petitions that relied on AI-invented rulings, so an invented citation is not a harmless slip.

**Judicial reform context (snapshot as of 2026-11-03; volatile).** Statuses below change week to week. Treat each as "as of 2026-11-03" and as unverified until you check it. Before stating any of them, check at the Supreme Court rulings search (https://supremedecisions.court.gov.il/) and the Knesset legislation database (https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/lawlaws.aspx?t=lawlaws&st=lawlaws): whether the measure was enacted and published in Reshumot, what its commencement provision says, for a bill its current stage and any continuity decision, and any court order affecting it. Where a status rests on press reports, say so, and say which of these checks you could not complete. Three distinct strands must not be conflated:

1. *Reasonableness amendment strike-down (2024-01-01).* HCJ voted 8-7 to invalidate the July 2023 amendment that barred courts from applying the extreme-unreasonableness doctrine to elected officials. In the same judgment, a separate, large majority (reported as 12 of 15) held that HCJ has the authority to strike down Basic Laws in exceptional circumstances. Do NOT cite the 8-7 vote for the Basic-Laws authority point.
2. *Judicial Selection Committee reform (Basic Law amendment, March 2025).* It takes effect when the next Knesset begins its term. Elections for the 26th Knesset were set for 2026-10-27, and Basic Law: The Knesset s.12 requires the new Knesset to convene within 14 days of election day. Do not say the 26th Knesset has convened, or that the amended composition is in force, unless you have checked that it has. Petitions against the amendment were pending before an 11-justice HCJ panel as of 2026-11-03 (press reports of conditional orders); check for a ruling before saying which composition governs.
3. *Judicial Overhaul Redux (2026 legislative push).* A connected set of measures, each at a DIFFERENT stage, do not lump them together as "pending bills":
   - **Mahash (Police Investigation Department) law, ENACTED (final reading 2026-06-11).** Press reports of 2026-09-04 describe an HCJ interim order freezing its leadership, appointment and separate-budget provisions until a hearing on the petitions set for 2026-12-28. Check the case status before saying whether any provision is in force.
   - **AG split bill, first reading only (June 2026, per press reports).** Not enacted by the 25th Knesset. It survives only if the continuity rule (דין רציפות) is applied: a government formed in the new Knesset, or for a committee or private bill the committee, must announce in the plenum its wish to apply it, and for an MK's bill that MK must sit in the new Knesset and consent (Continuity of Bills Law 1993, ss.1-3). It is eligible because it passed first reading.
   - **Ministerial legal advisers bill, preliminary reading only (2026-01-07, per press reports).** Continuity applies only to bills that passed first reading, so it does not carry over.
   - **Civil Service Commissioner:** press reports of 2026-02-04 describe an HCJ ruling that the government is NOT required to appoint the commissioner through a competitive process.
   Any answer about who has legal-advisory authority must flag the exact status of each item, and must NOT present a mid-process bill as law, a lapsed bill as pending, or a frozen provision as operative.

Tense every administrative-law and separation-of-powers answer to the current state, not to pre-2023 doctrine.

## Instructions

### Step 1: Understand the Legal Question
Classify the query:
- **Legislation lookup:** Which law or regulation applies?
- **Concept explanation:** What does a Hebrew legal term mean?
- **Procedure guidance:** What court, what process, what deadlines? Use `references/court-procedure-map.md` (which court, appeal routes, filing). For a defects dispute, first ask whether the user bought from the developer or hired a contractor, because a different statute applies.
- **Document preparation:** Structure for a contract, claim, or notice? Give the required parts and the principles the user drafts from, never a completed pleading or contract for the user's live matter.
- **Rights inquiry:** What are someone's rights in a given situation?

### Step 2: Identify the Area of Law
Israeli law is organized by area:
| Area | Key Legislation | Hebrew |
|------|----------------|--------|
| Constitutional | Basic Laws; judicial review of ordinary statutes rests on CA 6821/93 United Mizrahi Bank v. Migdal (decided 9.11.1995) | Chukei Yesod |
| Contract | Contracts Law (General Part) 1973 | Chok HaChozim |
| Employment | Employment laws bundle, incl. Protection of Wages Law 1958 (late-wage compensation, s.17) and the 2008 mandatory-pension extension order | Chukei Avoda |
| Real Estate | Land Law 1969 (the Superintendent of Land Registration decides the disputes between apartment owners specified in s.72(a), on rights and duties under the provisions it lists or the by-laws, not every condominium claim; for the trespass disputes specified in s.72(b) the plaintiff may choose a competent court or the Superintendent), Planning Law 1965 | Chok HaMikrkain |
| New-apartment defects | Sale (Apartments) Law 1973 (s.4 inspection and warranty periods, s.4A one-year notice for visible defects, s.4B repair opportunity); Contractor Contract Law 1974 if the owner hired the contractor | Chok HaMecher (Dirot), Chok Chozeh Kablanut |
| Corporate | Companies Law 1999 | Chok HaChevarot |
| Consumer | Consumer Protection Law 1981 (with multiple amendments including recent updates for digital commerce) | Chok Haganat HaTzarchan |
| Privacy | Privacy Protection Law 1981 (Amendment 13, published 14.8.2024, in force August 14, 2025 under s.74(a) of the amending law, with exceptions in s.74(b): independent Privacy Protection Authority enforcement; expanded DPO duties; a severe security incident must be reported to the PPA immediately under the Privacy Protection (Data Security) Regulations 2017, reg. 11(d)(1), the basis of the PPA's fines for late reporting; the PPA's Menora notice states that this duty does not wait for a technical investigation or a finding of fault (not the GDPR 72-hour wording); significant administrative fines (for the tariff figures consult the PPA's Amendment-13 guide, do not quote from memory). Damages without proof of harm: s.29A up to NIS 50,000, double only where intent to harm is proven, index-linked from May 2007; Amendment 13's new s.15A exemplary damages up to NIS 10,000. The PPA publishes its Amendment-13 fines on its gov.il site, e.g. NIS 256,000 on Menora Mivtachim for late reporting (notice published 22/10/26, https://www.gov.il/he/pages/menora-221026: a NIS 640,000 base cut by a cumulative 60% on reduction grounds the PPA found in that case); cite enforcement examples only from the PPA's own notices, and do not present one case's amount or reductions as a tariff) | Chok Haganat HaPratiut |
| Torts | Torts Ordinance (New Version) | Pkudat HaNezikin |
| Family | Various personal status laws | Dinei Mishpacha |
| Tax | Income Tax Ordinance, VAT Law | Pkudat Mas Hachnasa, Chok Maam |
| Administrative | Administrative Courts Law 2000 (petitions on matters in its First Schedule go to the District Court sitting as an Administrative Court, not to the HCJ, s.5) | Chok Batei Mishpat LeInynaim Minhaliyim |
| Courts & Procedure | Courts Law 1984 (small claims: individual plaintiffs, s.60; lawyer only by leave, s.63; appeal only by leave, s.64), Civil Procedure Regulations 2018 | Chok Batei HaMishpat, Takanot Seder HaDin |
| Limitations | Limitation Law 1958 (7 years non-land; land 15 or 25 years by registration type, but the Limitation Law does not apply to claims to realize a right in settled land, Land Law s.159(b), save pleas that accrued before 1.1.1970, and contractual or unregistered-right claims connected with land need separate analysis; s.15A Swords of Iron: for non-land claims not yet expired on 25.1.2024, 7.10.2023 to 6.4.2024 is not counted; land claims only if their period would have ended between 25.1.2024 and 6.4.2024; read s.15A and its conditions before applying it) | Chok HaHityashnut |

### Step 3: Research and Present
When researching:
1. Start with the primary legislation (the "chok" or "pkuda")
2. Note relevant amendments (tikunim) and their dates
3. Reference key court rulings (psikot din) if relevant. Find them in the free Supreme Court search (supremedecisions.court.gov.il, rulings from 1997) or Nevo/Takdin. Before calling a holding controlling, check it was the holding and not obiter, and check for a later further hearing (diyun nosaf) or departure. Basic Law: The Judiciary s.20: a Supreme Court holding binds all courts except the Supreme Court; other courts' holdings only guide courts below them
4. Explain in plain language first, then provide Hebrew legal terms
5. Link to public sources when available (Knesset website, Kol Zchut)

### Step 4: Provide Context
For every legal research response:
- State which law(s) apply. Cite section numbers (saifim) ONLY when you have verified them against a source; if you are not certain of the exact saif, name the law and tell the user where to confirm the section ([source]) instead of guessing a number (this follows the anti-hallucination rule above, never emit an unverified saif just to fill the slot)
- Note if the law has been recently amended
- Mention if there are pending legislative changes
- Suggest specific sections of Kol Zchut for free detailed information
- Recommend consulting an orech din for specific cases

### Documents and sensitive data
- When the user authorizes work with their documents (contracts, court papers, agency letters, or health, rehabilitation, insurance or claim records), handle the records the task needs through authorized tools and storage, within the existing scope of access and applicable privacy requirements. Use only the details needed, keep personal identifiers out of public-source searches unless the lookup itself needs them, and avoid unnecessary copies or sensitive content in logs. Ask again only when a new disclosure, destination or access expansion needs authorization.
- Treat dates, amounts and deadlines read from a notice, letter or judgment, or flagged by a parsing tool, as candidates to check, not legal determinations. The date printed on a notice is not necessarily the date it was served (המצאה) or the day a period starts: find the governing provision and the event it counts from, and say when that event is unknown. State a deadline as fact only after verifying the provision for that specific procedure.
- This skill holds no health, insurance, benefit or rehabilitation eligibility rules, so do not state eligibility, amounts or deadlines for such programmes from it; research the governing text and say what remains unverified.

## Hebrew Legal Terminology Reference
| Hebrew | English | Context |
|--------|---------|---------|
| chok | law/statute | Primary legislation by Knesset |
| pkuda | ordinance | Pre-state legislation still in force |
| takana | regulation | Secondary legislation by minister |
| psak din | court ruling | Only its holding (halacha), not obiter, has precedential effect: a Supreme Court holding binds every court except the Supreme Court; another court's holding guides courts below it (Basic Law: The Judiciary s.20) |
| bagatz | High Court of Justice | Supreme Court sitting as HCJ |
| tvia | claim/lawsuit | Filing a legal action |
| ktav tvia | statement of claim | Opening document in civil case |
| ktav hagana | statement of defense | Defendant's response |
| orech din | attorney/lawyer | Licensed legal practitioner |
| roeh cheshbon | accountant | Certified public accountant |
| notar | notary | Public notary |
| saif | section | Section of a law |
| saif katan | subsection | Subsection of a law |

## Examples

### Example 1: Employment Rights Question
User says: "What severance pay is an employee entitled to in Israel?"
Result: Explain Severance Pay Law 1963 (Chok Pitzuei Piturin): s.12(a) gives one month's salary per year to a salaried (monthly) employee and states a lower statutory rate for wage (hourly/daily) employees that regulations under s.12(b) may raise (check the current rule before stating a figure), conditions for entitlement, how pension savings interact with severance (Section 14 arrangement). Recommend Kol Zchut page and consulting an employment lawyer.

### Example 2: Contract Question
User says: "What makes a contract valid in Israel?"
Result: Explain Contracts Law (General Part) 1973: offer (hatzaa), acceptance (kibul), consideration not required in Israeli law (unlike common law), good faith requirement (tom lev), void vs. voidable contracts.

### Example 3: Starting a Business
User says: "What legal structure should I use for a startup in Israel?"
Result: Compare options: Chevra Baam (Ltd company), Shutfut (partnership), Osek Morsheh/Patur (sole proprietor). Explain Companies Law 1999 requirements, registration with Companies Registrar (Rasham HaChevarot).

## Bundled Resources

### Scripts
- `scripts/legal_term_lookup.py`, Interactive Hebrew legal terminology database with 53 terms covering courts, legislation types, legal proceedings (including small claims, leave to appeal, further hearing), professionals, contract law, employment law, and property law. Look terms up by transliteration, English, or Hebrew (e.g. `--term "בג\"ץ"`); also area-filtered listing and full dictionary display. Run: `python scripts/legal_term_lookup.py --help`

### References
- `references/court-procedure-map.md`, Which court hears what, the appeal map (as of right vs. leave), what binds as precedent, filing and costs pointers, and a worked routing for construction-defect disputes (developer vs. hired contractor). Consult for any "which court / how do I file / can I appeal" question.
- `references/legal-databases-guide.md`, Comprehensive guide to Israeli legal research databases including paid platforms (Nevo, Takdin, Psakdin) and free resources (Knesset portal, Court rulings portal, Kol Zchut, Bituach Leumi). Consult when the user needs to find legislation text, court rulings, or rights information and you need to recommend the right source.
- `references/legislation-index.md`, Index of key Israeli legislation organized by area (constitutional, contract, employment, corporate, real estate, consumer, tort, privacy, tax, criminal, administrative) with Hebrew names, key section numbers, and practical notes. Consult when you need to identify which specific law applies to a user's question.

## Gotchas

- Israeli laws are referenced by their Hebrew year of enactment (e.g., תשמ"א / tashma"a = 1981; תשמ"ב / tashma"b = 1982), not the Gregorian year. Agents may cite the wrong law when searching by year number alone.
- The Israeli legal system is a mixed system (not pure common law or civil law) with its own statutory precedent rule. Under Basic Law: The Judiciary s.20, a holding of a court guides courts below it (s.20(a)), and a holding of the Supreme Court binds every court except the Supreme Court itself (s.20(b)) (Sefer HaChukkim 1110, 1984, pp.80-81); only the holding, not obiter, has that effect. Do not import US/UK assumptions such as jury trials (Israel has none) or their precedent hierarchy, and do not tell users that precedent does not bind in Israel.
- Kol Zchut (All Rights, kolzchut.org.il) is a well-regarded free secondary source for Israeli rights information, not the law itself: use it to explain and to find the statute or official source it cites, then rely on and cite that source.
- Israeli court decisions are cited by a leading proceeding abbreviation + docket number, then the party names, then the official reporter reference where one exists, or for an unreported ruling the database and decision date (e.g., ע"א 4628/93 מדינת ישראל נ' אפרופים שיכון וייזום (1991) בע"מ, פ"ד מט(2) 265: case 4628 filed in 1993). A slash docket is number/year, not year/number; newer dockets use a number-MM-YY shape. Copy the docket exactly as printed and do not convert between shapes. Do not drop the party names, and never invent a docket number or a פ"ד reference; take both from a database hit.
- Many Israeli laws from the British Mandate era (pkudot) are still in force. Agents may assume pre-1948 legislation is obsolete when it is not.
- The 2024-01-01 HCJ judgment had TWO separate votes. The 8-7 vote struck down the reasonableness amendment. A separate, large majority (reported as 12 of 15) held that HCJ has authority to strike down Basic Laws in narrow circumstances. Agents routinely conflate the two and cite "8-7" for the Basic-Laws-review authority point. Cite each holding to its own count, taken from the judgment itself rather than from news reports.
- Contract-interpretation doctrine shifted with Amendment 3 to the Contracts Law (General Part) (third reading 2026-01-05; published 7.1.2026, Sefer HaChukkim 3481, p.212). Section 25(a) now has TWO versions, selected by contract DATE: contracts made up to 6.1.2026 keep the prior Apropim-era rule; for contracts made or renewed from 7.1.2026, the parties' own agreement on interpretation governs, and absent one a BUSINESS contract (חוזה עסקי) is read by its language alone unless that is unreasonable or self-contradictory. Non-business, standard-form (חוזה אחיד) and employment contracts are still read by the parties' intent, and parties not represented by a lawyer in drafting are treated as not having agreed on an interpretation method. Check the contract date and type before applying either rule. This summary was not checked against the published text for this skill: read the amendment, including its application provision, before relying on it.
- The 2025 Judicial Selection Committee amendment takes effect when the 26th Knesset begins its term (elections set for 2026-10-27; first sitting within 14 days by Basic Law: The Knesset s.12). As of 2026-11-03 the HCJ petitions were pending. Before answering "who appoints judges", check whether the new Knesset has convened and whether the HCJ has ruled; never state a future sitting as having happened.
- The 2026 "judicial-overhaul-redux" measures are at DIFFERENT stages, do not blanket-label them. The Mahash law is ENACTED, but press reports describe key provisions frozen by an HCJ interim order (2026-09-04) pending a 2026-12-28 hearing; check the case status. The AG-split bill passed only a first reading and needs the continuity rule to survive into the new Knesset; the ministerial-legal-advisers bill passed only a preliminary reading and does not carry over. Check the Knesset portal for the current stage of each before citing.
- A defect question about a new apartment is governed by the Sale (Apartments) Law 1973, not the 1974 Assurance of Investments law, which only secures the buyer's payments. Ask about the one-year notice for visible defects (s.4A) before anything else, and check whether the building was completed or the contract signed before 06.04.2011 (then the pre-2011 version and its inspection-period table apply). The inspection and warranty periods are LIABILITY periods, not filing deadlines; the claim itself is subject to the Limitation Law (s.6 start; s.8 delays the start only where the facts were unknown to the claimant for reasons beyond their control that even reasonable care could not have prevented).

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Knesset legislation portal | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/lawlaws.aspx?t=lawlaws&st=lawlaws | Primary Israeli legislation, amendments (tikunim) |
| Kol Zchut | https://www.kolzchut.org.il | Rights and benefits wiki in Hebrew, Arabic, English |
| Nevo | https://www.nevo.co.il | Comprehensive (paid) Israeli legal database |
| Takdin | https://www.takdin.co.il | Alternative (paid) legal database |
| Supreme Court rulings search | https://supremedecisions.court.gov.il/ | Free search of Supreme Court rulings and decisions from 1997, by text or docket |
| Bituach Leumi (NII) | https://www.btl.gov.il | Social security benefits, entitlements and appeals |

## Troubleshooting

### Error: "Cannot access Nevo/Takdin"
Cause: These are paid databases requiring subscription
Solution: Use free alternatives: Knesset legislation portal, the Supreme Court rulings search (supremedecisions.court.gov.il), Kol Zchut wiki. Note that free sources may not be as comprehensive. If a citation cannot be confirmed in any reachable source, say so instead of producing one.

### Error: "Law may have been amended"
Cause: Israeli laws are frequently amended; information may be outdated
Solution: Always recommend verifying current version on Knesset website or Nevo. Note the last known amendment date.
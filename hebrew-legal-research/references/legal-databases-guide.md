# Israeli Legal Databases Guide

## Overview
This guide covers the primary legal databases and resources available for
Israeli legal research, including both paid and free options.

## Paid Databases

### Nevo (nevo.co.il)
- **Publisher:** Nevo Publishing Ltd.
- **Coverage:** Comprehensive: legislation, case law, legal articles, secondary sources
- **Strengths:**
  - Most comprehensive Israeli legal database
  - Full text of all Knesset legislation (current and historical versions)
  - Supreme Court, District Court, and specialized court rulings
  - Legal articles and commentary
  - Advanced search with Hebrew morphological analysis
  - Cross-references between legislation and case law
- **Access:** Subscription required (monthly/annual)
- **URL:** https://www.nevo.co.il
- **API integration:** This skill has no verified API integration for this provider. Use authorized portal access; check the provider's current documentation and access terms before programmatic access.
- **Tips for researchers:**
  - Use the "consolidated version" (nusach meshulav) for current law text
  - Check amendment history (tikunim) for recent changes
  - Use the "related rulings" feature to find relevant case law

### Takdin (takdin.co.il)
- **Publisher:** Takdin Legal Database Ltd.
- **Coverage:** Legislation, case law, legal forms
- **Strengths:**
  - Strong case law collection
  - Legal forms and templates
- **Access:** Subscription required
- **URL:** https://www.takdin.co.il
- **API integration:** This skill has no verified API integration for this provider. Use authorized portal access; check the provider's current documentation and access terms before programmatic access.
- **Tips for researchers:**
  - Good alternative when Nevo is unavailable
  - Form templates useful for document preparation

### Psakdin (psakdin.co.il, spelled "Pskdin" in some places)
- **Publisher:** Psakdin Ltd.
- **Coverage:** Court rulings focus
- **Strengths:**
  - Specialized in court rulings
  - Summary and analysis of significant rulings
- **Access:** Subscription required
- **URL:** https://www.psakdin.co.il

## Free Resources

### Knesset Legislation Portal
- **Publisher:** The Knesset (Israeli Parliament)
- **Coverage:** All primary legislation passed by the Knesset
- **Strengths:**
  - Free access to all legislation text
  - Official source for law text
  - Legislative history and committee discussions
  - Bills (hatzaot chok) tracking
- **Limitations:**
  - May not always have the most recent consolidated version
  - Search functionality is basic
  - No case law
- **URL:** https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/lawlaws.aspx?t=lawlaws&st=lawlaws
- **Tips:**
  - Use for verifying official law text
  - Check Reshumot (official gazette) for publication dates
  - Committee protocols provide legislative intent context

### Court Rulings (Judicial Authority)
- **Publisher:** Israeli Judicial Authority (הרשות השופטת)
- **Coverage:** Supreme Court rulings and decisions; selected lower-court rulings
- **Strengths:**
  - Free Supreme Court search by free text or by docket number: rulings and decisions from 1997 onward, plus rulings published in the official reporter (פד"י) volumes from 2006 (volume סא) onward
  - Recent rulings published quickly
- **Limitations:**
  - Not all lower-court rulings are published; historical coverage before 1997 is incomplete
  - Search is limited compared to commercial databases
  - The sites run a WAF that blocks many bots and some foreign IPs. Distinguish a rendering or connection failure from an explicit access denial. For a public page the current tool cannot render, use an authorized supported browser or another full official publication. Stop a route that explicitly denies access or shows a browser security warning; do not change headers, proxies or security settings to evade it. Record the exact source gap, and ask the user for the text only if no authorized retrieval route is available.
- **URLs:**
  - Supreme Court rulings search: https://supremedecisions.court.gov.il/
  - Supreme Court site: https://supreme.court.gov.il/ (opens the Supreme Court home page with a recent rulings list)
  - Judicial Authority portal: https://www.court.gov.il now redirects to https://www.gov.il/he/departments/the_judicial_authority, which links to the rulings search for the Supreme Court and the other courts, and to digital filing
  - Court fees reference: https://www.gov.il/he/pages/fees_16
- **Tips:**
  - Supreme Court (Bagatz and civil/criminal appeals) best covered
  - Older Supreme Court slash dockets are **number/year**: ע"א 4628/93 is case 4628 filed in 1993 (decided in 1995), and older Bagatz petitions follow the same pattern (בג"ץ 5100/94). Newer dockets use a number-MM-YY shape. Copy the docket exactly as printed in the judgment or database hit; do not convert between shapes or rebuild one from memory
  - Before treating a holding as controlling, check for a later further hearing (דיון נוסף) or a later ruling that departed from it

### Kol Zchut (kolzchut.org.il)
- **Publisher:** Kol Zchut (All Rights) non-profit, with the support of the Ministry of Justice and the National Digital Agency
- **Coverage:** Legal rights information wiki
- **Strengths:**
  - Free, comprehensive rights information
  - Written in accessible Hebrew (not legalese)
  - Covers employment, housing, health, social security, consumer rights
  - Regularly updated
- **Limitations:**
  - Not a primary legal source
  - Simplified explanations may miss nuances
  - Not suitable for advanced legal research
- **URL:** https://www.kolzchut.org.il
- **Tips:**
  - Excellent starting point for understanding rights
  - Each article links to relevant legislation
  - Good for client-facing explanations

### National Insurance Institute (btl.gov.il)
- **Publisher:** Bituach Leumi (National Insurance Institute)
- **Coverage:** Social security rights and benefits
- **Strengths:**
  - Official information on all NII benefits
  - Calculators for benefit amounts
  - Application forms and procedures
- **URL:** https://www.btl.gov.il

## Research Methodology

### Step 1: Identify the Legal Area
Determine which area of law is relevant (contract, employment, tort, etc.)

### Step 2: Find Primary Legislation
Use Knesset portal or Nevo to locate the relevant chok or pkuda

### Step 3: Check Current Version
Verify you have the consolidated version including all amendments (tikunim)

### Step 4: Find Relevant Case Law
Search for Supreme Court interpretations of the relevant sections

### Step 5: Check Secondary Sources
Look for legal articles and commentary explaining the law

### Step 6: Verify Currency
Confirm no recent amendments or pending legislation changes

## Citation Format
Israeli legal citations typically follow this format:
- **Legislation:** Chok [Name], [Hebrew year]-[Gregorian year], Sefer HaChukim [number], amud [page]
- **Court ruling:** [Court/proceeding abbreviation] [docket number exactly as printed: number/year, or number-MM-YY for newer dockets] [Party 1] נ' [Party 2], and where the ruling was published in the official reporter, פ"ד [volume]([part]) [page]
- **Example:** ע"א 4628/93 מדינת ישראל נ' אפרופים שיכון וייזום (1991) בע"מ, פ"ד מט(2) 265 (1995)
- **Example:** בג"ץ 5100/94 הוועד הציבורי נגד עינויים בישראל נ' ממשלת ישראל (the respondents are the Government and the General Security Service, not "the State of Israel")
- **Unreported ruling** (most recent rulings have no פ"ד reference): proceeding abbreviation, docket number as printed, party names, then the database and the decision date as shown in the hit, for example (נבו <date>). State the panel, and whether the passage you rely on is the majority holding or a minority or concurring opinion, because Basic Law: The Judiciary s.20(b) binds only the holding.
- Always copy the exact docket number, party names and reporter reference from a verified source; never reconstruct them from memory. If no database is reachable, say the citation could not be confirmed.

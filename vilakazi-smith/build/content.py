"""All site copy and firm facts in one place. Edit here, then run `python3 build/build.py`.

Only facts the firm has confirmed belong in FIRM and OFFICES. Leave a value as None to keep it off the site.
"""

DOMAIN = "https://www.vsinc.co.za"
LASTMOD = "2026-10-13"

FIRM = {
    "name": "Vilakazi Smith Inc.",
    "legal_name": "Vilakazi Smith Incorporated",
    "short": "VSI",
    "founded": "2020",
    "slogan": "Take action.",
    "bbbee": "B-BBEE Level 2 (125% procurement recognition)",
    "main_phone": "012 492 5505",
    "postal": "Postnet Suite 484, Private Bag X1007, Lyttelton, 0140",
    "email": None,          # TBC: enquiry email (kept out of the page code to avoid spam harvesters; the form sends it)
    "hours": None,          # TBC: office hours
    "social": [],           # TBC: Facebook / LinkedIn URLs
}

OFFICES = [
    {
        "slug": "pretoria",
        "name": "Pretoria",
        "title": "Attorneys in Pretoria",
        "lines": ["Cambridge Office Park, Building 32", "Ground Floor (Right)", "5 Bauhinia Street, Highveld Techno Park", "Centurion, 0157"],
        "street": "Cambridge Office Park, Building 32, Ground Floor (Right), 5 Bauhinia Street, Highveld Techno Park",
        "locality": "Centurion",
        "postcode": "0157",
        "phones": [("012 492 5505", "+27124925505"), ("012 492 5506", "+27124925506")],
        "fax": "086 577 5456",
        "map_q": "Cambridge Office Park, 5 Bauhinia Street, Highveld Techno Park, Centurion, 0157",
        "areas": ["Pretoria", "Midrand"],
        "meta_title": "Attorneys in Pretoria | Vilakazi Smith Inc. Law Firm",
        "meta_desc": "Vilakazi Smith Inc. attorneys in Pretoria, at Highveld Techno Park: family, labour, criminal, commercial, insurance, property and estate law. Call 012 492 5505.",
        "intro": [
            "Our Pretoria office in Highveld Techno Park is the firm's main office. All of our records and files are managed here, so every matter, whichever office you visit, is run from Pretoria.",
            "It is convenient for clients across Pretoria and Midrand.",
        ],
    },
    {
        "slug": "sandton",
        "name": "Sandton",
        "title": "Attorneys in Sandton",
        "lines": ["2nd Floor, 66 Park Lane", "Sandown", "Sandton, 2196"],
        "street": "2nd Floor, 66 Park Lane, Sandown",
        "locality": "Sandton",
        "postcode": "2196",
        "phones": [("010 979 4130", "+27109794130")],
        "fax": "086 577 5456",
        "map_q": "66 Park Lane, Sandown, Sandton, 2196",
        "areas": ["Sandton", "Johannesburg", "Randburg"],
        "meta_title": "Attorneys in Sandton, 66 Park Lane | Vilakazi Smith Inc.",
        "meta_desc": "Vilakazi Smith Inc. at 66 Park Lane, Sandown, Sandton: commercial, labour, family, criminal, insurance, property and estate law. Call 010 979 4130.",
        "intro": [
            "Our Sandton office at 66 Park Lane in Sandown gives clients in Johannesburg's northern suburbs a place to meet their attorney close to home or work.",
            "Files for Sandton clients are managed by our central team in Pretoria, so you get the same service and the same record-keeping wherever you consult us.",
        ],
    },
]

# Each practice area has its own page. `services` come from the firm's current website.
PRACTICE = [
    {
        "slug": "family-law",
        "name": "Family & matrimonial law",
        "short": "Divorce, maintenance, children's court, protection orders and antenuptial contracts.",
        "img": "pa-family.webp",
        "img_alt": "Paper cut-out family of three standing beside a judge's gavel",
        "h1": "Family law attorneys in Pretoria & Sandton",
        "meta_title": "Family & Divorce Attorneys, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Divorce, maintenance, children's court matters, protection orders and antenuptial contracts. Family law attorneys in Pretoria and Sandton.",
        "lead": "Clear, steady advice when your family's future is on the line: divorce, maintenance, children and the agreements that protect you before you marry.",
        "body": [
            "Family matters are personal and often urgent. We explain your rights and options in plain language, work towards a settlement where one is possible, and represent you firmly in court where it is not.",
            "We act in the High Court, the Regional Court and the Maintenance and Children's Courts.",
        ],
        "services": [
            ("Divorce proceedings", "Opposed and unopposed divorces, settlement agreements and the division of the estate."),
            ("Maintenance court proceedings", "Applications for child and spousal maintenance, and increases, reductions and enforcement."),
            ("Children's court proceedings", "Care, contact and guardianship, and parenting plans."),
            ("Domestic violence and harassment proceedings", "Applications for protection orders and harassment orders, and opposing them."),
            ("Antenuptial contracts", "Choosing your marital property system and drafting and registering your antenuptial contract."),
        ],
        "faqs": [
            ("How long does a divorce take in South Africa?",
             "An unopposed divorce, where both spouses have signed a settlement agreement, can usually be finalised within a few weeks to a few months, depending on the court's roll. An opposed divorce takes much longer, often a year or more, because the court has to decide the issues the spouses cannot agree on."),
            ("Do I need an antenuptial contract?",
             "If you marry without an antenuptial contract, your marriage is automatically in community of property: your estates are combined and you share each other's debts. An antenuptial contract lets you marry out of community of property, with or without the accrual system. It must be signed before a notary before the wedding and registered at the Deeds Office."),
            ("How is child maintenance worked out?",
             "Both parents have a legal duty to support their children according to their means. The court looks at the child's reasonable needs, such as housing, food, school and medical costs, and at each parent's income and expenses, then divides the cost between the parents."),
        ],
    },
    {
        "slug": "banking-finance-law",
        "name": "Banking, finance & securities",
        "short": "Bond registration and cancellation, foreclosures, business rescue and insolvency.",
        "img": "pa-banking.webp",
        "img_alt": "Attorney and clients discussing documents beside a brass scale of justice",
        "h1": "Banking & finance attorneys in Pretoria & Sandton",
        "meta_title": "Banking & Finance Attorneys, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Bond registration and cancellation, foreclosures, Section 129 notices, business rescue and insolvency. Attorneys in Pretoria and Sandton.",
        "lead": "Security for lenders and a clear way forward for borrowers and businesses in financial distress.",
        "body": [
            "We handle the legal work around secured lending, from registering a bond to cancelling it once it is paid up, and the proceedings that follow when an account falls into arrears.",
            "For businesses under financial pressure, we help assess whether business rescue is a realistic option and guide you through insolvency where it is not.",
        ],
        "services": [
            ("Registration and cancellation of bonds", "Mortgage bonds and other security registered at, and cancelled through, the Deeds Office."),
            ("Foreclosure proceedings", "Recovering secured debt, from the Section 129 notice through to judgment and execution."),
            ("Business rescue assistance", "Advice for companies, directors and creditors on Chapter 6 business rescue proceedings."),
            ("Insolvency-related matters", "Claims, creditor meetings and disputes in liquidations and sequestrations."),
        ],
        "faqs": [
            ("What is a Section 129 notice?",
             "A Section 129 notice is a letter a credit provider must send under the National Credit Act before it can take legal action on a defaulted credit agreement, such as a home loan. It tells you that you are in arrears and sets out your options, including going to a debt counsellor or reaching a payment arrangement. Get advice as soon as you receive one."),
            ("Can the bank sell my home if I fall behind on my bond?",
             "Only through a court process. The bank must first obtain judgment, and when the property is your primary home, the court must also consider whether it may be sold in execution and whether a reserve price should be set. Acting early gives you more options."),
            ("What is business rescue?",
             "Business rescue, under Chapter 6 of the Companies Act, is a process for a financially distressed company. A business rescue practitioner takes over supervision of the company and draws up a plan to restore it or achieve a better result for creditors than liquidation. While it runs, legal action against the company is generally suspended."),
        ],
    },
    {
        "slug": "wills-estates-trusts",
        "name": "Wills, estates & trusts",
        "short": "Wills, estate administration, insolvent estates, curatorships and trusts.",
        "img": "pa-wills.webp",
        "img_alt": "Fountain pen resting on a handwritten document",
        "h1": "Wills & estates attorneys in Pretoria & Sandton",
        "meta_title": "Wills & Estates Attorneys, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Wills, deceased estates, insolvent estates, curatorships and trusts. Wills and estates attorneys in Pretoria and Sandton.",
        "lead": "Plan properly now, and your family is spared the delay and cost of sorting out your affairs later.",
        "body": [
            "A valid, up-to-date will is the simplest way to make sure your assets go to the people you choose. We draft wills and trusts that fit your family and your estate, and we administer deceased estates through the Master of the High Court.",
            "When someone can no longer manage their own affairs, we bring curatorship applications so that a trusted person can act for them.",
        ],
        "services": [
            ("Drafting wills and testaments", "Wills drafted to meet the formal requirements of the Wills Act and to reflect your wishes."),
            ("Estate administration", "Reporting the estate to the Master, and the liquidation and distribution accounts through to finalisation."),
            ("Winding up insolvent estates", "Administering deceased estates whose debts exceed their assets."),
            ("Curatorship applications", "Court applications to appoint a curator for a person unable to manage their own affairs."),
            ("Trusts", "Drafting, registering and administering inter vivos and testamentary trusts."),
        ],
        "faqs": [
            ("What makes a will valid in South Africa?",
             "Under the Wills Act, a will must be in writing and signed at the end by the person making it, with every page signed. It must be signed in the presence of two competent witnesses, aged 14 or older, who are both present at the same time and who also sign. A witness, or their spouse, should not be a beneficiary."),
            ("What happens if someone dies without a will?",
             "The estate is then divided according to the Intestate Succession Act, which sets out who inherits, starting with the surviving spouse and children. This may not match what the person would have wanted, and it can slow the administration down."),
            ("How long does it take to wind up a deceased estate?",
             "Straightforward estates are often finalised in six to twelve months. Estates with property, businesses, disputes or tax issues usually take longer. The timeline depends on the Master's Office, SARS and how quickly documents are provided."),
        ],
    },
    {
        "slug": "commercial-law",
        "name": "Commercial law",
        "short": "Commercial litigation, debt collection, contracts, liquidations, sequestrations and evictions.",
        "img": "pa-commercial.webp",
        "img_alt": "Glasses and a pen on an open notebook beside a laptop",
        "h1": "Commercial law attorneys in Pretoria & Sandton",
        "meta_title": "Commercial Lawyers, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Commercial litigation, debt collection, contracts, liquidations, sequestrations and evictions. Commercial attorneys in Pretoria and Sandton.",
        "lead": "Practical legal support for businesses: sound agreements up front, and firm action when payment or performance doesn't follow.",
        "body": [
            "We advise businesses of all sizes on the agreements they sign and the disputes that follow. Where a matter can be settled, we settle it; where it cannot, we litigate.",
            "We also act for landlords and owners in eviction proceedings, following the procedure the law requires so the order stands.",
        ],
        "services": [
            ("Commercial litigation", "Contractual and commercial disputes in the Magistrates' and High Courts."),
            ("Debt collection", "Letters of demand, summons, judgment and recovery."),
            ("Contractual claims", "Claims for breach of contract, damages and specific performance."),
            ("Drafting, vetting and settling commercial agreements", "Shareholder, supply, service, lease and other commercial agreements."),
            ("Liquidations and sequestrations", "Applications to wind up companies and sequestrate individuals' estates."),
            ("Evictions", "Residential and commercial evictions, following the correct court procedure."),
        ],
        "faqs": [
            ("How does debt collection through an attorney work?",
             "It usually starts with a letter of demand. If the debt is not paid or settled, we issue summons in the Magistrates' or High Court, depending on the amount, and obtain judgment. The judgment can then be enforced through the sheriff, for example by attaching assets. Most ordinary debts prescribe after three years, so do not wait too long."),
            ("What is the difference between liquidation and sequestration?",
             "Both are insolvency processes. Liquidation applies to companies and close corporations. Sequestration applies to individuals, partnerships and trusts, under the Insolvency Act."),
            ("Can I evict a tenant without a court order?",
             "No. Evicting someone from their home requires a court order under the Prevention of Illegal Eviction from and Unlawful Occupation of Land Act (PIE). The occupier must receive proper notice of the proceedings, and the court must be satisfied that eviction is just and equitable. Changing the locks or cutting off services yourself is unlawful."),
        ],
    },
    {
        "slug": "labour-law",
        "name": "Labour law",
        "short": "CCMA and bargaining council matters, employment contracts, retrenchments and disciplinary inquiries.",
        "img": "pa-labour.webp",
        "img_alt": "Shelves of leather-bound law reports",
        "h1": "Labour law attorneys in Pretoria & Sandton",
        "meta_title": "Labour Law & CCMA Attorneys, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "CCMA and bargaining council representation, employment contracts, retrenchments and disciplinary hearings. Labour attorneys in Pretoria and Sandton.",
        "lead": "Fair process protects both the employer and the employee. We help you get it right, and represent you when it is challenged.",
        "body": [
            "We advise employers on contracts, policies and procedures that hold up, and represent parties at the CCMA, bargaining councils and the Labour Court.",
            "We also chair disciplinary inquiries independently, so the outcome rests on a fair hearing.",
        ],
        "services": [
            ("CCMA representation", "Conciliation and arbitration of dismissal and unfair labour practice disputes."),
            ("Bargaining council litigation", "Disputes in the bargaining council for your sector."),
            ("Employment contracts and policies", "Contracts of employment, workplace policies and disciplinary codes."),
            ("Retrenchment processes", "Facilitating consultation under Section 189 of the Labour Relations Act."),
            ("Chairing disciplinary inquiries", "Independent chairpersons for disciplinary and incapacity hearings."),
        ],
        "faqs": [
            ("How long do I have to refer an unfair dismissal dispute to the CCMA?",
             "You must refer an unfair dismissal dispute to the CCMA, or to the bargaining council for your sector, within 30 days of the date of dismissal. Unfair discrimination disputes must be referred within six months. A late referral needs a condonation application, so act quickly."),
            ("Can an attorney represent me at the CCMA?",
             "Not at conciliation. At arbitration, legal representation is allowed in most disputes, but in dismissals about conduct or capacity it is only allowed if the commissioner permits it or the parties agree. We can still prepare you and your case, and represent you wherever representation is allowed."),
            ("What makes a retrenchment fair?",
             "The employer needs a genuine operational reason and must follow the consultation process in Section 189 of the Labour Relations Act: notice inviting consultation, a meaningful joint attempt to avoid or reduce job losses, fair and objective selection criteria, and severance pay of at least one week's pay for each completed year of service."),
        ],
    },
    {
        "slug": "criminal-law",
        "name": "Criminal law",
        "short": "Bail applications, plea and sentence agreements, criminal trials and expungements.",
        "img": "pa-criminal.webp",
        "img_alt": "Two people seated in a wood-panelled courtroom",
        "h1": "Criminal defence attorneys in Pretoria & Sandton",
        "meta_title": "Criminal Lawyers & Bail, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Police and formal bail applications, plea agreements, criminal trials and expungements. Criminal defence attorneys in Pretoria and Sandton.",
        "lead": "From the first hours after an arrest to the end of a trial, you need an attorney who acts quickly and knows the process.",
        "body": [
            "The first steps after an arrest often shape the rest of the case. We assist with bail at the police station and in court, advise you on your rights, and represent you through plea negotiations or trial.",
            "Years after a conviction, we also help clients apply to have qualifying criminal records expunged.",
        ],
        "services": [
            ("Police bail applications", "Applications for bail at the police station for qualifying offences, at any hour."),
            ("Formal bail applications", "Bail applications in court, including for more serious offences."),
            ("Plea and sentence agreements", "Negotiating agreements with the prosecution under Section 105A of the Criminal Procedure Act."),
            ("Criminal litigation", "Defence in the Magistrates', Regional and High Courts."),
            ("Expungement of criminal records", "Applications to remove qualifying older convictions from your record."),
        ],
        "faqs": [
            ("What is the difference between police bail and formal bail?",
             "For certain less serious offences, the police can grant bail at the station before your first court appearance. For other offences, bail must be applied for in court, where the magistrate decides whether to release you and on what conditions. The more serious the offence, the more you must show for bail to be granted."),
            ("What is a plea and sentence agreement?",
             "Under Section 105A of the Criminal Procedure Act, an accused person, through their legal representative, can agree with the prosecution on the charge they will plead guilty to and on the sentence. The court must still be satisfied that the agreement and the sentence are just before it accepts them."),
            ("Can my criminal record be expunged?",
             "Some older convictions for less serious offences can be expunged once ten years have passed since the conviction, if there has been no further conviction in that time. The application is made to the Department of Justice. Whether you qualify depends on the sentence you received."),
        ],
    },
    {
        "slug": "insurance-law",
        "name": "Insurance law",
        "short": "Rejected claims, FAIS Ombud referrals, policy reviews, recoveries and insurance litigation.",
        "img": "pa-insurance.webp",
        "img_alt": "A brass Lady Justice statuette on a desk while a document is signed",
        "h1": "Insurance law attorneys in Pretoria & Sandton",
        "meta_title": "Insurance Claim Lawyers, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Rejected insurance claims, FAIS Ombud complaints, policy reviews, recoveries and insurance litigation. Attorneys in Pretoria and Sandton.",
        "lead": "When a claim is rejected or a policy is not what you were told, we help you understand where you stand and challenge the decision.",
        "body": [
            "Insurance disputes turn on the wording of the policy and the facts of the claim. We review both, give you a clear legal opinion, and take the matter further through the insurer's internal process, the ombuds or the courts.",
            "We also act in recoveries, where loss caused by a third party is recovered from that party.",
        ],
        "services": [
            ("Referring complaints to the FAIS Ombud", "Complaints about financial advisers and intermediaries."),
            ("Appealing the outcome of claims", "Challenging rejected or under-settled claims."),
            ("Short- and long-term insurance reviews and negotiations", "Policy reviews and negotiation with insurers."),
            ("Recoveries", "Recovering losses from the third party responsible."),
            ("Legal opinions", "Written opinions on cover, liability and prospects of success."),
            ("Insurance litigation", "Court action on insurance claims and disputes."),
        ],
        "faqs": [
            ("My insurance claim was rejected. What can I do?",
             "Ask the insurer for its reasons in writing and check them against your policy wording. You can then use the insurer's internal complaints process, approach the relevant ombud or go to court. Policies often contain time limits for challenging a rejection, so get advice promptly."),
            ("What is the FAIS Ombud?",
             "The FAIS Ombud handles complaints against financial service providers, such as financial advisers and brokers, under the Financial Advisory and Intermediary Services Act. For example, it deals with complaints about advice that led you to buy an unsuitable policy. Complaints about how an insurer handled a claim go to a different ombud."),
            ("Do I need an attorney to dispute an insurance claim?",
             "Not always, but a legal opinion early on helps you understand whether the rejection is justified and which route is likely to work best. If the matter has to go to court, or the amount is significant, legal representation is strongly advisable."),
        ],
    },
    {
        "slug": "conveyancing-property-law",
        "name": "Conveyancing & real estate",
        "short": "Property transfers, mortgage bonds, subdivisions, consolidations and sectional title extensions.",
        "img": "pa-conveyancing.webp",
        "img_alt": "Attorney pointing to a document beside a model building",
        "h1": "Conveyancing attorneys in Pretoria & Sandton",
        "meta_title": "Conveyancing Attorneys, Pretoria & Sandton | Vilakazi Smith",
        "meta_desc": "Property transfers, bond registrations, subdivisions, consolidations and sectional title extensions. Conveyancers in Pretoria and Sandton.",
        "lead": "Registering a property is the final step of a sale. We keep it moving, and keep buyers, sellers and banks informed along the way.",
        "body": [
            "We handle property transfers and bond registrations at the Deeds Office, from the signed offer to purchase through to registration.",
            "For owners and developers, we also deal with subdivisions, consolidations and extensions of sectional title units.",
        ],
        "services": [
            ("Transfer of properties", "Residential and commercial property transfers, from instruction to registration."),
            ("Registration of mortgage bonds", "Registering bonds for buyers and banks."),
            ("Subdivision and consolidation", "Splitting or joining land units after municipal approval."),
            ("Extension of sectional title units", "Registering extensions to sectional title units and schemes."),
        ],
        "faqs": [
            ("How long does a property transfer take?",
             "A typical transfer takes about two to three months from the signed offer to purchase to registration at the Deeds Office. The time depends on bond approval, the cancellation of the seller's bond, rates and levy clearance certificates, and the Deeds Office's workload."),
            ("Who pays the transfer costs?",
             "The buyer usually pays the transfer duty (payable to SARS on properties above the exemption threshold) and the conveyancing fees for the transfer, and the bond registration costs if they are taking a home loan. The seller usually pays to cancel their existing bond and to obtain the required compliance certificates."),
            ("What is subdivision or consolidation of land?",
             "Subdivision splits one piece of land into two or more separate erven; consolidation combines adjacent erven into one. Both need approval from the municipality under its land-use rules, a surveyor's diagram, and registration at the Deeds Office."),
        ],
    },
]

HOME_FAQS = [
    ("How do I book a consultation?",
     "Call our Pretoria office on 012 492 5505 or our Sandton office on 010 979 4130, or send a consultation request through our contact page. Tell us briefly what your matter is about and which office suits you."),
    ("Which office should I visit?",
     "Choose whichever is more convenient for you: Pretoria, at Highveld Techno Park, or Sandton at 66 Park Lane, Sandown. All files are managed centrally from our Pretoria office, so you receive the same service at either one."),
    ("What should I bring to my first consultation?",
     "Bring your ID and any documents related to your matter, such as contracts, letters, court papers, policy documents or title deeds, along with a short timeline of what happened."),
    ("Do you assist individuals and businesses?",
     "Yes. We act for individuals in family, criminal, estate and property matters, and for businesses in commercial, banking, insurance and labour matters."),
]

# Shown until the firm supplies verified testimonials (with each client's written permission).
TESTIMONIALS = [
    ("[Client testimonial: one or two sentences in the client's own words.]", "[Client name]", "[Role], [Company]"),
    ("[Client testimonial: one or two sentences in the client's own words.]", "[Client name]", "[Role], [Company]"),
    ("[Client testimonial: one or two sentences in the client's own words.]", "[Client name]", "[Role], [Company]"),
    ("[Client testimonial: one or two sentences in the client's own words.]", "[Client name]", "[Role], [Company]"),
]

# Team placeholders: the firm's team details are out of date, so names and photos stay blank until confirmed.
TEAM = [
    ("[Attorney name]", "[Director / Attorney]", "[One-sentence bio: admission, qualifications and practice focus.]"),
    ("[Attorney name]", "[Attorney]", "[One-sentence bio: admission, qualifications and practice focus.]"),
    ("[Attorney name]", "[Attorney / Conveyancer]", "[One-sentence bio: admission, qualifications and practice focus.]"),
]

ABOUT = [
    "Vilakazi Smith Incorporated (VSI) was founded in 2020 and holds a B-BBEE Level 2 certificate (125% B-BBEE procurement recognition).",
    "Although we have a presence in both Johannesburg and Pretoria, all our operations are centralised in Pretoria, where all records and files are managed.",
    "We prioritise providing exceptional legal and business services while staying attuned to the practical challenges our clients and their customers face every day. Our philosophy centres on delivering outstanding legal and business solutions through personal interaction, resolving matters professionally and decisively, and always seeking the most cost-effective approach.",
]

MISSION = ("Our mission is to give every client the best possible service.",
           "At Vilakazi Smith Incorporated, our mission is to deliver top-tier legal services tailored to each client's needs. With a steadfast commitment to integrity, professionalism and client satisfaction, we provide innovative solutions that uphold justice, protect rights and drive favourable outcomes. Through our expertise, dedication and adherence to ethical standards, we aim to build lasting partnerships, guiding clients through legal complexities so they can achieve their goals with confidence.")

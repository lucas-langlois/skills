# Original-publication retrieval

## Identity before acquisition

Use tools actually available in the session; check current provider documentation before relying on API details. Verify DOI resolution and compare title, authors, publication year and venue against the manuscript entry. A resolving DOI may identify a different paper. Crossref metadata is useful for identity, not for establishing full-text support:
https://www.crossref.org/documentation/retrieve-metadata/rest-api/

For missing or suspect identifiers, search the exact title and authors through publisher pages, Crossref or a suitable scholarly index. Retain candidate matches and explain ambiguity. Do not invent a replacement DOI or declare fabrication from one failed lookup. Non-DOI publications can be genuine. Record online-first versus issue dates without silently changing the reference.

Check the publisher record for corrections, retractions and related versions; record checks that could not be completed. A correction may require reading both the article and its notice.

## Acquisition routes

1. Check authorized project reference folders and available reference-manager attachments, including EndNote exports/linked PDFs and Zotero where accessible. Do not recursively scan unrelated personal directories or alter libraries.
2. Follow the verified DOI to the publisher's accessible article HTML or PDF. Full article HTML is acceptable; an abstract landing page is not full text.
3. Look for a lawful open-access copy in an institutional/subject repository or author repository using the exact identity. Suitable discovery services may include Unpaywall, OpenAlex, Europe PMC or PMC when relevant. Discover their available tools/documentation rather than assuming API access. If a service requires an email or credential, use only a legitimately supplied one; otherwise use another route.
4. When only an accepted manuscript or preprint is accessible, identify it as such and check version correspondence. Do not present preprint evidence as the published version. Material differences or uncertain correspondence limit the verdict.
5. If no accessible complete copy is found after the relevant routes and one targeted title/author repository search, log the attempts and mark full text unavailable. Continue the audit and list the exact publication needed from the author. Retry only when new access information becomes available.

Use existing authorized institutional access only when available through supplied tools. An access denial is a retrieval outcome, not evidence that the article does not exist or does not support a claim. Do not substitute another paper without explicit scope to find replacements.

### Institutional and browser access

When the user has authorized access through an institution-connected network or browser session, try the publisher directly in the session's supported browser before assuming a subscription article is inaccessible. Network-based institutional recognition may require no login. Record any publisher statement identifying institutional access, but verify access separately for each article/publisher; one successful retrieval is not evidence of access to all journals. Use existing authorized sessions and leave manual authentication/MFA to the user when tools or policy require it. If a CAPTCHA or robot check requires human interaction, ask the user to complete it and resume afterward; do not bypass the challenge.

Use the browser tools prescribed by the current environment. A generic web fetch or terminal request may have different network/session access from the browser; failure there does not establish browser access failure. Read full article HTML directly where usable. A PDF is optional: download it when needed for figures/tables, reliable extraction, page evidence or reproducibility. Use the publisher's PDF link through the authorized browser session; if browser tooling requires saving an already accessible response via a download link/blob, preserve the original publication URL and verify response type and PDF signature. Confirm the completed download's actual filesystem path before copying it. Never export session cookies or credentials to another tool merely to reproduce access.

## Acquisition validation and provenance

For each work, record reference ID, manuscript bibliography text, verified identifier, verified title/authors/year, landing URL, actual acquisition URL or local route, access time, copy/version, local path, SHA-256 hash and access status. For browser-only HTML with no saved copy, leave local path/hash explicitly unavailable, retain a stable URL and section/text locators, and disclose that preservation limitation; do not invent a file or require PDF saving for an otherwise adequate check. For blob downloads retain both the publisher PDF URL and temporary browser download URL. For local copies with unknown download origin, say so.

Check response content and the saved document itself: a login/challenge page saved with a `.pdf` extension is not a paper. Confirm article identity from its contents, completeness of relevant sections, and whether supplements required by the claim are accessible. Record extraction quality, OCR use and omissions. Do not infer complete reading from successful extraction.

PDF evidence locators should distinguish physical PDF pages from printed article pages. HTML evidence uses headings, table/figure IDs and text anchors, with a saved snapshot where tools permit. Verify tables, equations and figures visually when text extraction distorts them. An unreadable scan remains unverifiable unless reliable OCR and original-page checking recover the needed evidence.

Retain originals separately from derived text; do not overwrite earlier versions. Cache retrieval once per work, but audit each citation occurrence independently. Keep the manifest up to date so interrupted work can resume without pretending unfinished claims have been checked.

# Policy Mask - XML PII Redaction Tool

Masks personally identifiable information (PII) from insurance policy XML files, replacing sensitive data with `XXX` characters for safe sharing and debugging.

## Features

- Masks insured names, addresses, phone numbers, and emails
- Masks financial data (bank accounts, credit cards, BSB numbers)
- Masks policy/quote numbers and external references
- Masks intermediary and agent details
- Masks underwriter comments and audit logs
- Preserves XML structure for testing/debugging
- No external dependencies — uses Python standard library only

## Usage

```bash
python mask_policy.py input.xml output_masked.xml
```

If no arguments provided, defaults to reading `policy.xml` and writing `policy_masked.xml`.

## What Gets Masked

| Category | Fields |
|----------|--------|
| Personal | Insured names, trading name, contact name |
| Address | Street, suburb, postcode (insured + locations) |
| Contact | Phone numbers, email addresses |
| Financial | BSB, account number, account name, credit card |
| Policy | Policy number, quote number, external references |
| Users | User IDs, audit log entries |
| Intermediary | Account numbers, email addresses |
| Comments | Underwriter notes |

## Example

Input:
```xml
<Insured1Name><Value>John Smith</Value></Insured1Name>
```

Output:
```xml
<Insured1Name><Value>XXXXXXXXXX</Value></Insured1Name>
```

## Requirements

- Python 3.6+
- No external packages needed

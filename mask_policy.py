import xml.etree.ElementTree as ET
import sys

def mask_value(text):
    if not text or not text.strip():
        return text
    return 'X' * len(text.strip())

def mask_policy_xml(input_file, output_file):
    # Read file and skip any non-XML header lines (e.g., browser copy-paste headers)
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the first line that starts with '<' (actual XML content)
    xml_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('<'):
            xml_start = i
            break

    xml_content = ''.join(lines[xml_start:])
    root = ET.fromstring(xml_content)
    tree = ET.ElementTree(root)

    mask_paths = [
        './/Insured/Insured1Name/Value',
        './/Insured/Insured2Name/Value',
        './/Insured/Insured3Name/Value',
        './/Insured/TradingName/Value',
        './/Insured/PreviousInsured1Name',
        './/Insured/ContactName/Value',
        './/Address/Address1/Value',
        './/Address/Address2/Value',
        './/Address/Postcode/Value',
        './/Address/Suburb/Value',
        './/Location/Address1/Value',
        './/Location/Address2/Value',
        './/Location/Postcode/Value',
        './/Location/Suburb/Value',
        './/Phone/Number/Value',
        './/Email/Value',
        './/EmailAddress',
        './/ConsentForContact/Name/Value',
        './/ConsentForContact/Email/Value',
        './/ConsentForContact/PhoneNumber/Value',
        './/Client/Name/Value',
        './/Client/Code/Value',
        './/Client/GSTDetails/ABN/Value',
        './/Intermediary//AccountNumber/Value',
        './/Intermediary//AccountName/Value',
        './/Intermediary//EmailAddress',
        './/User/Userid/Value',
        './/AuditLogs/Userid',
        './/PolicyNumber/Value',
        './/QuoteNumber/Value',
        './/PreviousQuoteNumber/Value',
        './/OldPolicyNumber/Value',
        './/DirectDebit/BSB/Value',
        './/DirectDebit/AccountNumber/Value',
        './/DirectDebit/AccountName/Value',
        './/CreditCard/Name/Value',
        './/CreditCard/Number/Value',
        './/BankerId/Value',
        './/ExternalReferenceNumber/Value',
        './/UnderwriterComments//User/Value',
        './/UnderwriterComments//Note/Value',
        './/PrintDelivery/EmailAddress/Value',
        './/SMELeadData/InsuredName/Value',
        './/SMELeadData/ClientEmail/Value',
        './/SMELeadData/ClientPhone/Value',
        './/SMELeadData/BankerId/Value',
    ]

    for path in mask_paths:
        for elem in root.findall(path):
            if elem.text and elem.text.strip():
                elem.text = mask_value(elem.text)

    for attr in ['extMessageId', 'extBrokerPolicyId', 'extBrokerSiteId', 'extInsurerSiteId']:
        if root.get(attr):
            root.set(attr, 'MASKED')

    tree.write(output_file, xml_declaration=True, encoding='utf-8')
    print(f"Masked XML written to: {output_file}")

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'policy.xml'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'policy_masked.xml'
    mask_policy_xml(input_file, output_file)

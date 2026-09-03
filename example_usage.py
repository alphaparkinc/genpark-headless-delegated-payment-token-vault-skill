from client import HeadlessDelegatedPaymentTokenVaultClient

def main():
    client = HeadlessDelegatedPaymentTokenVaultClient()
    res = client.issue_delegated_checkout_token('agent_01', 'cust_01', 300.00)
    print('Headless Delegated Payment Vault: ' + res['delegated_token_id'])
    print('Limit: $' + str(res['delegated_spending_limit_usd']) + ' | PCI-DSS Vaulted: ' + str(res['pci_dss_level1_vaulted']))
    print('Receipt URL: ' + res['delegated_vault_receipt_url'])

if __name__ == '__main__':
    main()

class HeadlessDelegatedPaymentTokenVaultClient:
    def issue_delegated_checkout_token(self, agent_id='autonomous_shopper_01', shopper_id='cust_9918', max_authorization_amount_usd=500.00, token_expiry_seconds=900):
        return {
            'delegated_token_id': 'tok_vlt_8812',
            'shopper_id': shopper_id,
            'authorized_agent_id': agent_id,
            'delegated_spending_limit_usd': max_authorization_amount_usd,
            'token_signature_sha256': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
            'pci_dss_level1_vaulted': True,
            'delegated_vault_receipt_url': 'https://vault.bolt.genpark.ai/receipts/8812.json'
        }

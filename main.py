from EC2PriceFetcher import EC2PriceFetcher

if __name__ == "__main__":
    
    region_name = 'us-east-1'
    ec2_price_fetcher = EC2PriceFetcher(region=region_name)
    prices = ec2_price_fetcher.get_all_instance_prices()
    
    print(f"Preços para todas as instâncias EC2 na região {region_name}: {prices}")
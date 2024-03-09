import boto3

class EC2PriceFetcher:
    def __init__(self, region='us-east-1'):
        self.region = region
        self.pricing_client = boto3.client('pricing', region_name=self.region)

    def get_all_instance_prices(self):
        response = self.pricing_client.get_products(
            ServiceCode='AmazonEC2'
        )

        prices = []
        for product in response['PriceList']:
            terms = product.get('terms', {}).get('OnDemand', {})
            for term_key, term_value in terms.items():
                price_dimensions = term_value.get('priceDimensions', {})
                for dimension_key, dimension_value in price_dimensions.items():
                    price = float(dimension_value.get('pricePerUnit', {}).get('USD', 0.0))
                    prices.append(price)

        return prices
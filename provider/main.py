from provider.provider_factory import ProviderFactory


def main():
    choice = input("Enter a Bank Provider\n")
    provider = ProviderFactory.create_provider(choice)
    return provider
    

if __name__ == "__main__":
    main()
    
    
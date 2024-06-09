from tld import get_tld

class UrlHandler:
    def __init__(self, url) -> dict:
        self.url = url
        self.subdomain = ""
        self.domain_name = ""
        self.domain = ""
        self.domain_extension = ""
        self.domain_data = None
        
        self.extract_domain_info()
        self.get_dict_data()

    def extract_domain_info(self):
        extracted_data = get_tld(self.url, as_object=True, fail_silently=True)
        self.domain_data = extracted_data

    def get_dict_data(self):
        self.subdomain = self.domain_data.subdomain if self.domain_data.subdomain else None
        self.domain_name = self.domain_data.fld
        self.domain_extension = self.domain_data.tld
        self.domain = self.domain_name.replace("." + self.domain_extension, "")
        return {
            "subdomain": self.subdomain,
            "domain_name": self.domain_name,
            "domain": self.domain,
            "domain_extension": self.domain_extension
        }
    def __repr__(self):
        return str(self.get_dict_data())

url_handler = UrlHandler("http://rajannedfgh.sdgjh.co.in")
print(url_handler)

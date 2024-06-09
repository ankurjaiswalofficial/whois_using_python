import PyFunceble

class DomainChecker:
    def __init__(self, domain):
        self.domain = domain
        self.status = None
        self.expiration_date = None
        self.registered = None
        self.nameservers = None
        self.raw = None

        self.check_domain()

    def check_domain(self):
        result = PyFunceble.domain(self.domain, complete=True)

        if result:
            self.status = result.get("status")
            self.expiration_date = result.get("expiration_date")
            self.registered = result.get("registered")
            self.nameservers = result.get("nameservers")
            self.raw = result

    def get_info(self):
        return {
            'domain': self.domain,
            'status': self.status,
            'expiration_date': self.expiration_date,
            'registered': self.registered,
            'nameservers': self.nameservers,
            'raw': self.raw
        }

    def __repr__(self):
        return str(self.get_info())

# Example usage:
if __name__ == "__main__":
    domain_checker = DomainChecker("example.com")
    print(domain_checker)


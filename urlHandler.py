from tld import get_tld

def extract_domain_info(link):
    domain = get_tld(link, as_object=True, fail_silently=True)
    subdomain = domain.subdomain if domain.subdomain else None
    domain_name = domain.fld
    domain_extension = domain.tld

    return subdomain, domain_name, domain_extension

# Example usage:
link = "http://some..hello.ibn.subdomain.google.co.uk"
subdomain, domain, domain_extension = extract_domain_info(link)
print("Subdomain:", subdomain)
print("Domain:", domain)
print("Domain Extension:", domain_extension)

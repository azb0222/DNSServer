dig: command used to do DNS queries, get DNS information about domain anmes, IP addresses, DNS servers. sends a DNS query request, communicates with DNS server to get requested information 

## Authoritative DNS Server (Authoritative Name Server) 
provides up to do DNS records 
store DNS records for the domains they are authoritative for: 
- A Record: map hostname --> IPv4 address 
- AAAA Record: map hostname --> IPv6 address 
- CNAME Record: provide aliast for hostname 
- NS Record: list authoritative name servers for domain 
  
DNS resolver needs to resolve domain name --> queries root DNS server --> goes to appropriate TLD (top level domain server) --> goes to authortitave DNS server responsible for the specific domain 

authoritiatve DNS servers use zone files to store DNS records for a domain  

RR: Resource Record. specific resource associated with a domain name. RRs are organized into DNS zones. 
RR format: 
1) Name 
2) Type (A, AAAA, MX, CNAME, etc)
3) Data  

### Message Compression 
 
reduce the amount of bandwidth a DNS request sends 
import pyfiglet
import whois
import sys
ascii_banner = pyfiglet.figlet_format("Who tool")
print(ascii_banner)
print("WHOIS CREADO POR TRIPLE YEI")

n = len(sys.argv)
print("name " , sys.argv[0])
print("argument passed", end = " ")

for i in range(1,n):
	print(sys.argv[i], end = " " )

domain = sys.argv[1]

w = whois.whois(domain)

print(w)

	

	
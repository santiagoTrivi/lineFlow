from math import exp
from math import factorial




# Class to calculate the summatory of rho^x/factorial(x)
class BaseQueueProcedure:
	def PnSumatory(rho: float, servers: float) -> float:
		sumatoria=0
		for x in range(servers):
			calculo = rho**x/factorial(x)
			sumatoria = sumatoria + calculo
		return sumatoria


#####################################
## multiple server queues unlimited
#####################################

def PzeroUnlimited(rho: float, servers: float) -> float:
	sumatoria= BaseQueueProcedure.PnSumatory(rho, servers)
	expresion = rho**servers/(factorial(servers)*(1-rho/servers))
	resultado = 1.0/(sumatoria + expresion)
	return resultado




def ProbPn_Unlimited(lambda_,mu,servers,n, Po):
	Pn = 0
	rho = lambda_ / mu
	if(n<=servers and n>=0):
		Pn = (rho**n/factorial(n))*Po
	if(n>servers):
		Pn = ((rho**n)/((servers**(n-servers))*factorial(servers)))*Po
	return Pn

def calculate_prob_dist_unlimited(lambda_, mu, servers ,Po):
    prob_dist = []
    Fn = 0
    n = 0

    while Fn < 0.9999 or Fn == 1:
        Pn = ProbPn_Unlimited(lambda_, mu, servers, n, Po)
        Fn += Pn
        prob_dist.append({"n": n, "Pn": Pn, "Fn": Fn})
        n += 1

    return prob_dist

def multiple_calculate_unlimited(lambda_, mu, servers):
	rho = lambda_ / mu

	if rho >= servers:
		raise ValueError(f"Rho ({rho}) debe ser menor que la cantidad de servidores ({servers}).")

	Po = PzeroUnlimited(rho, servers)
	Lq = (((lambda_*mu)*((lambda_/mu)**servers))/(factorial(servers-1)*((servers*mu-lambda_)**2)))*Po
	Ls = Lq + rho
	Wq = Lq / lambda_
	Ws = Wq + 1/mu
	return {
        "Lambda": lambda_,
        "Mu": mu,
        "Rho": rho,
        "Po": Po,
        "Ls": Ls,
        "Lq": Lq,
        "Ws": Ws,
        "Wq": Wq,
		"Prob_dist": calculate_prob_dist_unlimited(lambda_, mu, servers ,Po)
    }


###################################
## multiple server queues limited
###################################

def PzeroLimited(rho: float, servers: float, N: float) -> float:
	expresion = 0
	Pc = rho/servers
	sumatoria= BaseQueueProcedure.PnSumatory(rho, servers)
	if(Pc != 1):
		expresion = (rho**servers)*(1-(rho/servers)**(N-servers+1))/(factorial(servers)*(1-rho/servers))
	
	if(Pc == 1):
		expresion = ((rho**servers)/factorial(servers))*(N-servers+1)
	resultado = 1.0/(sumatoria + expresion)
	return resultado


def ProbPn_limited(lambda_,mu,servers,n, Po, N):
	Pn = 0
	rho = lambda_ / mu
	if(n<=servers and n>=0):
		Pn = (rho**n/factorial(n))*Po
	if(n<=N and n>=servers):
		Pn = ((rho**n)/(factorial(servers)*servers**(n-servers)))*Po
	return Pn


def InactiveServers(lambda_,mu,servers, Po, N):
	summatory = 0
	for x in range(servers + 1):
		Pn = ProbPn_limited(lambda_,mu,servers,x, Po, N)
		expresion = (servers-x)*Pn
		summatory = summatory + expresion
	return summatory

def LqLimited(rho, servers, Pzero, N):
	Pc = rho/servers
	Lq = 0
	if(Pc != 1):
		Lq = Pzero*(rho**(servers+1)/((factorial(servers-1))*(servers-rho)**2))
		expresion = (1 - ((Pc)**(N-servers)))-(N-servers)*((Pc)**(N-servers))*(1-Pc)
		Lq = Lq*expresion
	elif(Pc == 1):
		Lq = Pzero*(((rho**servers)*(N-servers)*(N-servers+1))/(2*factorial(servers)))
	return Lq


def calculate_prob_dist_limited(lambda_, mu, servers ,Po, N):
	prob_dist = []
	Fn = 0
	for n in range(N  + 1):
		Pn = ProbPn_limited(lambda_, mu, servers, n, Po, N)
		Fn += Pn
		prob_dist.append({"n": n, "Pn": Pn, "Fn": Fn})
	return prob_dist


def multiple_calculate_limited(lambda_, mu, servers, N):
	rho = lambda_ / mu
	Po = PzeroLimited(rho, servers, N)
	Lq = LqLimited(rho, servers, Po, N)
	inactiveServers = InactiveServers(lambda_, mu, servers, Po, N)
	Ls = Lq + (servers-inactiveServers)
	Wq = Lq / lambda_
	Ws = Wq + 1/mu
	Pn = ProbPn_limited(lambda_, mu, servers, N, Po, N)
	lambda_eff = lambda_ * (1 - Pn)
	lambda_loss = lambda_ - lambda_eff
	return {
		"Lambda": lambda_,
		"Mu": mu,
		"Rho": rho,
		"Po": Po,
        "inactive": inactiveServers,
		"Ls": Ls,
		"Lq": Lq,
		"Ws": Ws,
		"Wq": Wq,
		"Lambda_eff": lambda_eff,
		"lambda_loss": lambda_loss,
		"Prob_dist": calculate_prob_dist_limited(lambda_, mu, servers ,Po, N)
	}

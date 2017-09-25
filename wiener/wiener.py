import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0

            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Xong!")
                    return d

def test_hack_RSA():
	print "--------------------------------------------------------------------"
	print "Demo tan cong Wiener"
	print "--------------------------------------------------------------------"
	p, q, e, n, d = RSAvulnerableKeyGenerator.generateKeys(1024)
	print "p = ", p
	print "q = ", q
	print "n = ", n
	print "e = ", e
	print "d = ", d

	hacked_d = hack_RSA(e, n)

	if d == hacked_d:
		print("thanh cong!!")
	else:
		print("that bai :(")
	print "d ban dau: ", d
	print "d thu duoc: ", hacked_d
	return
    
if __name__ == "__main__":
    test_hack_RSA()





        
    

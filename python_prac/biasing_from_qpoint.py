print('This is program to find the biasing resistors using qpoint\n')
vce=int(input('please enter the value of collector voltage: \n'))
b=int(input('please enter the value of beta: \n'))
ie=float(input('please enter the value of collector current: \n'))
vcc=int(input('please enter the value of supply voltage: \n'))
vre=1
re=vre/ie
print('Emitter resistance value is {0} ohm'.format(re))
rc=(vcc-vce-ie*re)/ie
print('collector resistance value is {0} ohm'.format(rc))
ib=ie/b
print('base current value is {0} amps'.format(ib))
r1=(vcc-vre-0.7)/(10*ib)
print('R1 value is {0} ohm'.format(r1))
r2=(vre+0.7)/(9*ib)
print('R2 value is {0} ohm'.format(r2))



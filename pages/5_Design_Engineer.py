import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


st.set_page_config(page_title='Design Engineer')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Welcome to the Design Engineer Page!")

st.markdown(
    """
    Your role revolves around selecting the design parameters of the bike so as to maximize its stability. You
    will be provided with the set of the parameters with brief description.
    """)

st.markdown('---')

st.image('design_eng_1.png')
st.markdown('---')
st.image('design_eng_2.png')
st.markdown('---')
st.image('design_eng_3.png')
st.markdown('---')

# Input parameters
w = st.number_input('Insert Wheel base (m)', value=1.02)
c = st.number_input('Insert Trail (m)', value=0.08)
lamda = st.number_input('Steer axis tilt (rad)', value=np.pi/10)
g = st.number_input('Gravitational acceleration (N/kg or m/s)', value=9.81)
# %v=np.zeros((100, 1));% Forward velocity of bicycle (m/s)
# Rear wheel, R
rR = st.number_input('Radius (m)', value=0.3)
mR = st.number_input('Mass (kg)', value=2)
IRxx = st.number_input('Mass moments of inertia (kg m**2) ', value=0.0603)
IRyy = st.number_input('Mass moments of inertia (kg m**2)', value=0.0603)
# Read body and frame assembly, B
xB = st.number_input('Position of center of mass (m)', value=0.3)
zB = st.number_input('Position of center of mass (m)', value=-0.9)
mB = st.number_input('Mass (kg)', value=85)
IBxx = st.number_input('Mass moment of inertia (kg m**2)', value=9.2)
IByy = st.number_input('Mass moment of inertia (kg m**2)', value=11)
IBzz = st.number_input('Mass moment of inertia (kg m**2)', value=2.8)
IBxz = st.number_input('Mass moment of inertia (kg m**2)', value=0)
# Front handlebar and fork assembly, H
xH = st.number_input('Position of center of mass (m)', value=0.91)
zH = st.number_input('Position of center of mass (m)', value=-0.68)
mH = st.number_input('Mass (kg)', value=4)
IHxx = st.number_input('Mass moment of inertia (kg m**2)', value=0.05892)
IHyy = st.number_input('Mass moment of inertia (kg m**2)', value=0.12)
IHzz = st.number_input('Mass moment of inertia (kg m**2)', value=0.00708)
IHxz = st.number_input('Mass moment of inertia (kg m**2)', value=0, key=1)
# Front wheel, F
rF = st.number_input('Radius (m)', value=0.35)
mF = st.number_input('Mass (kg)', value=3)
IFxx = st.number_input('Mass moments of inertia (kg m**2)', value=0.1405)
IFyy = st.number_input('Mass moments of inertia (kg m**2)', value=0.1405, key=2)
# Calculation
# Total mass and center of mass location with respect to rear contact point p 

mT=mR+mB+mH+mF; # B 1
xT=(xB*mB+xH*mH+w*mF)/mT; # B 2
zT=(-rR*mR+zB*mB+zH*mH-rF*mF)/mT; # B 3 
# Relevant mass moments and products of inertia with respect to rear contact point P
ITxx=IRxx+IBxx+IHxx+IFxx+mR*rR**2+mB*zB**2+mH*zH**2+mF*rF**2; # B 4
ITxz=IBxz+IHxz-mB*xB*zB-mH*xH*zH+mF*w*rF; # B 5
IRzz=IRxx; IFzz=IFxx; # B 6
ITzz=IRzz+IBzz+IHzz+IFzz+mB*xB**2+mH*xH**2+mF*w**2; # B 7
# Total mass, center of location, and mass moment of inertia with respect to rear contact point P
mA=mH+mF; # B 8
xA=(xH*mH+w*mF)/mA; zA=(zH*mH-rF*mF)/mA; # B 9
IAxx=IHxx+IFxx+mH*(zH-zA)**2+mF*(rF+zA)**2; # B 10
IAxz=IHxz-mH*(xH-xA)*(zH-zA)+mF*(w-xA)*(rF+zA); # B 11
IAzz=IHzz+IFzz+mH*(xH-xA)**2+mF*(w-xA)**2; # B 12
# The center of mass of the front assembly form the center of mass of front wheel
uA=(xA-w-c)*np.cos(lamda)-zA*np.sin(lamda); # B 13
# Three special inertia quantities
IAll=mA*uA**2+IAxx*(np.sin(lamda))**2+2*IAxz*np.sin(lamda)*np.cos(lamda)+IAzz*(np.cos(lamda))**2; # A 14
IAlx=-mA*uA*zA+IAxx*np.sin(lamda)+IAxz*np.cos(lamda); # B 15
IAlz=mA*uA*xA+IAxz*np.sin(lamda)+IAzz*np.cos(lamda); # B 16
# The ratio of mechanical trail
nu=(c/w)*np.cos(lamda); # B 17
# Gyroscopic coefficients
SR=IRyy/rR; SF=IFyy/rF; ST=SR+SF; # B 18
SA=mA*uA+nu*mT*xT; # B 19
# Mass Matrix, M
M=np.zeros((2, 2));
M[0,0]=ITxx; M[0,1]=IAlx+nu*ITxz; M[1,0]=M[0,1]; 
M[1,1]=IAll+2*nu*IAlz+nu**2*ITzz; # A 20

# Gravity-dependent stiffness matrix, Ko
Ko=np.zeros((2, 2));
Ko[0,0]=mT*zT; Ko[0,1]=-SA; Ko[1,0]=Ko[0,1]; Ko[1,1]=-SA*np.sin(lamda); # B 22

# Velocity-dependent stiffness matrix, K2
K2=np.zeros((2, 2));
K2[0,0]=0; K2[0,1]=((ST-mT*zT)/w)*np.cos(lamda); K2[1,0]=0; 
K2[1,1]=((SA+SF*np.sin(lamda))/w)*np.cos(lamda); # A 24

# Damping-like matrix, C
C=np.zeros((2, 2));
C[0,0]=0; C[0,1]=nu*ST+SF*np.cos(lamda)+(ITxz/w)*np.cos(lamda)-nu*mT*zT; 
C[1,0]=-(nu*ST+SF*np.cos(lamda)); 
C[1,1]=(IAlz/w)*np.cos(lamda)+nu*(SA+(ITzz/w)*np.cos(lamda)); # B 26

########################################################
# Finding eigenvalues
v = sp.symbols('v', real=True)
sigma = sp.symbols('sigma', real=True)
EOM=M*sigma**2+v*C*sigma+g*Ko+v**2*K2;
EOM = sp.Matrix(EOM)
d = EOM.det()
s=sp.solveset(d, sigma)
vel=np.zeros((100,1));
sol=np.zeros((100,4), dtype=complex);
for i in range (1, 101):
    vel[i-1,0] = i/10;
    aa = s.subs(v, i/10) 
    sol[i-1,:] = np.fromiter(aa, dtype=complex)
########################################################
with st.spinner('Wait for it...'):
    plt.figure(figsize=(12, 8))
    plt.plot(vel, np.real(sol), linewidth=2)
    plt.plot(5.4995*np.ones((len(vel),1)), np.linspace(-30, 11,len(vel)), linestyle='--', linewidth=3)
    plt.plot(8.5345*np.ones((len(vel),1)), np.linspace(-30, 11,len(vel)), linestyle='--', linewidth=3)
    plt.title('Eigenvalue vs. velocity diagram of the benchmark model')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Real part of the eigenvalues')
    plt.grid(linestyle='-.')
st.pyplot()
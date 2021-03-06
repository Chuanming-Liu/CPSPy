import modesum, vmodel
import matplotlib.pyplot as plt

run =1
per=[10., 15., 20., 25., 30., 35., 40]
datatype='rho'
dm=-0.05
zmax=10.
wavetype='Love'
# wavetype='Rayleigh'



dset0 = modesum.modesumASDF()
dset0.getmodel(h=0.5 , zmax=100.)
if run:
    dset0.run_disp(workingdir='/home/leon/code/CPSPy/kerneltest_iso', outfname='/home/leon/code/CPSPy/kerneltest_iso_0.asdf', nmodes=1,
                period=per)
    dset0.run_eigen(infname='/home/leon/code/CPSPy/kerneltest_iso_0.asdf', outfname='/home/leon/code/CPSPy/kerneltest_iso_0.asdf')
dset0.load('/home/leon/code/CPSPy/kerneltest_iso_0.asdf')

model1 = dset0.model1d.copy()
model1.perturb(zmax=zmax, dm=dm, datatype=datatype)
# dset0.perturb(inmodel=dset0.model1d.copy(), wavetype='ray', perlst=[10., 20., 30., 40])

dset1 = modesum.modesumASDF()
dset1.getmodel(inmodel=model1)
if run:
    dset1.run_disp(workingdir='/home/leon/code/CPSPy/kerneltest_iso', outfname='/home/leon/code/CPSPy/kerneltest_iso_1.asdf', nmodes=1,
               period=per)
    dset1.run_eigen(infname='/home/leon/code/CPSPy/kerneltest_iso_1.asdf', outfname='/home/leon/code/CPSPy/kerneltest_iso_1.asdf')

dset1.load('/home/leon/code/CPSPy/kerneltest_iso_1.asdf')

c0, cpre, c = dset0.compare_disp(inmodel=model1, indbase=dset1, wavetype=wavetype, perlst=per)

fig, ax=plt.subplots()
plt.title(wavetype+' '+datatype+' perturb %g percent' %(dm*100)+' at top %g' %zmax +' km', fontsize=40)
plt.plot(per, c0, 'x--', lw=3, ms=10, label='m0')
plt.plot(per, cpre, 'o', ms=10, label='m1 predicted')
plt.plot(per, c, '^', ms=10, label='m1')
plt.legend(numpoints=1, fontsize=20, loc=0)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.ylabel('C (km/s)', fontsize=30)
plt.xlabel('Period (sec)', fontsize=30)
plt.show()
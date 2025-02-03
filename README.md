# dqcd-production

## Installation

Initialise the correct version of CMSSW
- GEN: CMSSW_13_2_0
- SIM to AOD: CMSSW_13_0_14
- miniAOD: CMSSW_13_0_14
- nanoAOD (see nanotron): CMSSW_13_3_0

e.g. for GEN, do

```
cmsrel CMSSW_13_2_0
cd CMSSW_13_2_0/src
cmsenv
````

Clone the repository with
```
git clone https://github.com/ic-dqcd/dqcd-production.git -b 2023 Configuration/GenProduction
```
or
```
git clone git@github.com:ic-dqcd/dqcd-production.git -b 2023 Configuration/GenProduction
````


Configure with
```
scram b -j8
```


Initialise your GRID certificate
```
voms-proxy-init --rfc --voms cms -valid 192:00
```

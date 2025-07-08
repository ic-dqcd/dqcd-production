# dqcd-production

## Installation

Initialise the correct version of CMSSW
- GEN: CMSSW_13_2_0
- GENSIM: CMSSW_13_0_20
- DIGI to RAW: CMSSW_13_0_14
- AOD: CMSSW_13_0_14
- following ones tbc:
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



## Specific case of IC servers
Due to the change of operative system to Alma EL9, a singularity must be used in order to load one of the available CMSSW versions available. In practice, the above instructions look like
```
/cvmfs/cms.cern.ch/common/cmssw-el7 # this opens the singularity
cmsrel CMSSW_13_2_0
cd CMSSW_13_2_0/src
cmsenv
git clone git@github.com:ic-dqcd/dqcd-production.git -b 2023 Configuration/GenProduction
scram b -j8
voms-proxy-init --rfc --voms cms -valid 192:00
```


##
For additional tools for submision and management, see
[https://github.com/jtafoya/dqcd-production-tools](https://github.com/jtafoya/dqcd-production-tools)


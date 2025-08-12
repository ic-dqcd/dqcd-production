# dqcd-production

## Production
This repository uses central production to generate the necessary samples. See

https://gitlab.cern.ch/cms-exo-mci/EXO-MCsampleRequests
https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-request#instructions

For it to work, we need EXO-MCsampleRequests to work with
- CMSSW_14_0_18
- --conditions 124X_mcRun3_2022_realistic_v12

## Installation

Clone the repository with
```
git clone git@github.com:ic-dqcd/dqcd-production.git -b 2024
````

Make a fork of EXO-MCsampleRequests and clone it to lxplus
(follow instructions as in https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-request)

Move the configuration files and request.csv to the corrrect directory in EXO-MCsampleRequests
```
cp dqcd-production/python/request.csv EXO-MCsampleRequests/
cp -r dqcd-production/python/ EXO-MCsampleRequests/genFragments/dqcd
```

Follow the tests as described in https://exo-mc-and-i.gitbook.io/exo-mc-and-interpretation/how-to-sample-request

## nanotron

Central samples are processed up to NANO level. However, these are not compatible with the `dqcd` framework, which need to be processed with `nanotron` instead. Luckly, central production stores some of the previous steps as well, including MINIAODSIM, which means that we simply need to process the very last step of the production.Processing should be done by hand as for 2022 and 2023.

As of today (1st of August 2025), the correct `nanotron` version to be used is Prijith's and using `CMSSW_15_0_2`.

To get the correct version of `nanotron`, do
```
cmsrel CMSSW_15_0_2
cd CMSSW_15_0_2/src
cmsenv
```
Then, pull and compile the correct version of the repo
```
git clone git@github.com:prijb/nanotron.git -b Parking nanotron # has some problems
git clone git@github.com:jaimeleonh/nanotron.git -b Parking24v15 nanotron # correct one at the moment! works well and already used to process the existent MiniAOD files.
scram build clean
scram build
```
See [https://github.com/prijb/nanotron/tree/Parking](https://github.com/prijb/nanotron/tree/Parking) for more details.

To run a production, be sure to load the following additional configuration, needed to rectify the proxy manager paths:
```
#Script for sourcing CMS related stuff
source /cvmfs/cms.cern.ch/cmsset_default.sh
export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
#New version
source /cvmfs/grid.cern.ch/alma9-ui-current/etc/profile.d/setup-alma9-test.sh
voms-proxy-init --rfc -voms cms --valid 192:00
```

The correct nanotron production configuration can be found in `dqcd-production/scripts/produceNANO.py`. Be sure to compare it with the default file, located in `CMSSW_15_0_2/src/nanotron/NANOProducer/test/produceNANO.py`, and replace it if necessary.

The config file `dqcd-production/scripts/cfg_creator_nano.py` is an assistant to submit the processing of the samples indicated within the file. It should be placed in `CMSSW_15_0_2/src/` (i.e. at the same depth as `nanotron`) and excecuted from there, i.e.
```
cd CMSSW_15_0_2/src
ln -s dqcd-production/scripts/cfg_creator_nano.py # you can also just copy it to the indicated directory
python3 cfg_creator_nano.py
```


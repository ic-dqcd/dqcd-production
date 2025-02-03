import os

p = "../data/"
files = os.listdir(p)

for f in files:
    name = f.split(".")[0]
    print(name)
    os.system("cp hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1_cfi.py %s_cfi.py" % name)
    os.system("sed -i 's/hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1/%s/g' %s_cfi.py" % (name, name))

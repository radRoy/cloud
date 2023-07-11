 1003  ls
 1004  cd data/
 1005  cd ~
 1006  module load anaconda3
 1007  source activate 3dunet
 1008  conda deactivate
 1009  ls
 1010  screen -ls
 1011  exit
 1012  screen -ls
 1013  git status
 1014  cd data/cloud/
 1015  git status
 1016  git push
 1017  git fetch
 1018  git pull
 1019  git status
 1020  git pull
 1021  git push
 1022  git status
 1023  bash pull-script.sh 
 1024  git pull
 1025  git fetch
 1026  git pull
 1027  git merge --abort
 1028  git fetch; git pull
 1029  git status
 1030  cd ..
 1031  ls
 1032  rm -r cloud
 1033  ls
 1034  ls -hal cloud
 1035  git clone git@github.com:radRoy/cloud.git
 1036  ls -a
 1037  git status
 1038  cd cloud/
 1039  git status
 1040  bash pull-script.sh 
 1041  screen -ls
 1042  ls
 1043  nano .gitignore
 1044  ls
 1045  git status
 1046  git add .gitignore 
 1047  git status
 1048  git add pytorch-3dunet/
 1049  git status
 1050  git rm --cached pytorch-3dunet
 1051  git status
 1052  git restore --staged pytorch-3dunet
 1053  git status
 1054  git submodule add https://github.com/wolny/pytorch-3dunet pytorch-3dunet
 1055  git status
 1056  git add pytorch-3dunet/
 1057  git status
 1058  git add pytorch-3dunet
 1059  git status
 1060  git add pytorch-3dunet/*
 1061  git status
 1062  git commit -m "try adding pytorch-3dunet as a submodule"
 1063  git status
 1064  git push
 1065  git status
 1066  ls -hal
 1067  git status
 1068  mv pytorch-3dunet ../
 1069  ls -hal
 1070  git status
 1071  git add .
 1072  git status
 1073  git commit -m "remove pytorch-3dunet from this repo"
 1074  git status
 1075  git push
 1076  git status
 1077  ls
 1078  git rm --cached pytorch-3dunet
 1079  git restore
 1080  git restore --staged 
 1081  git restore --staged .gitignore
 1082  git restore --staged pytorch-3dunet
 1083  git status
 1084  git restore --staged pytorch-3dunet/
 1085  ls -hal
 1086  git fetch
 1087  git pull
 1088  git status
 1089  git push
 1090  git status
 1091  bash pull-script.sh 
 1092  mkdir pytorch-3dunet
 1093  ls
 1094  cd ..
 1095  ls
 1096  cd pytorch-3dunet/
 1097  ls -hal
 1098  conda create -n 3dunet
 1099  module load anaconda3
 1100  conda create -n 3dunet
 1101  conda list
 1102  conda env list
 1103  conda remove testUnet
 1104  source activate 3dunet
 1105  pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
 1106  git clone https://github.com/wolny/pytorch-3dunet ~/data/
 1107  pip install -e ~/data/pytorch-3dunet/
 1108  pip install tensorboard
 1109  train3dunet
 1110  train3dunet --config data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml 
 1111  cd data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml
 1112  cd data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/
 1113  ls
 1114  cd ..
 1115  cp 3DUnet_lightsheet_boundary 3DUnet_lightsheet_boundary-original
 1116  mkdir 3DUnet_lightsheet_boundary-original
 1117  ls
 1118  cp 3DUnet_lightsheet_boundary/* 3DUnet_lightsheet_boundary-original/
 1119  ls 3DUnet_lightsheet_boundary
 1120  ls 3DUnet_lightsheet_boundary-original/
 1121  ls -hal 3DUnet_lightsheet_boundary
 1122  ls -hal 3DUnet_lightsheet_boundary-original/
 1123  cat 3DUnet_lightsheet_boundary/train_config.yml 
 1124  nano 3DUnet_lightsheet_boundary/train_config.yml 
 1125  ls
 1126  cat 3DUnet_lightsheet_boundary/train_config.yml 
 1127  ls
 1128  squeue
 1129  screen -ls
 1130  train3dunet --config data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml 
 1131  train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml 
 1132  cd 3DUnet_lightsheet_boundary
 1133  ls
 1134  nano train_config.yml 
 1135  train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml 
 1136  nano train_config.yml 
 1137  code
 1138  editor
 1139  module available
 1140  vscode
 1141  module load vscode
 1142  module list
 1143  code
 1144  vscode
 1145  snap --help
 1146  ls
 1147  cd ..
 1148  ls
 1149  cd ..
 1150  ls
 1151  ls -hal
 1152  ls -hal cloud/
 1153  ls
 1154  mv
 1155  mv --help
 1156  mv pytorch-3dunet cloud/
 1157  ls cloud
 1158  cd cloud/
 1159  ls pytorch-3dunet/
 1160  ls -a
 1161  ls -a pytorch-3dunet/
 1162  screen -S 3dunet_conda_create
 1163  screen -ls
 1164  screen --help
 1165  screen -wipe slurm_sessions_idk
 1166  screen -ls
 1167  screen -r slurm_sessions_idk 
 1168  screen -ls
 1169  .
 1170  screen -r git_cloud_outputs 
 1171  ls
 1172  cd data/
 1173  ls
 1174  ls cloud/
 1175  ls cloud/pytorch-3dunet/
 1176  ls -hal cloud/pytorch-3dunet/
 1177  ls -hal pytorch-3dunet/
 1178  cp --help
 1179  ls
 1180  cd pytorch-3dunet/
 1181  git status
 1182  git add .
 1183  git status
 1184  cat .gitignore
 1185  ls
 1186  cd ..
 1187  ls
 1188  cd cloud/
 1189  ls -lah
 1190  ls -lah pytorch-3dunet/
 1191  git status
 1192  git fetch
 1193  git pull
 1194  git status
 1195  bash commit-script.sh "try to copy pytorch-3dunet repo without the .git files etc."
 1196  git status
 1197  bash pull-script.sh 
 1198  git status
 1199  squeue --help
 1200  cd ~
 1201  ls
 1202  cd data/cloud
 1203  git status
 1204  bash pull
 1205  bah pull-script.sh 
 1206  bash pull-script.sh 
 1207  git status
 1208  screen -ls
 1209  screen unet-train-1
 1210  screen -S unet-train-1
 1211  screen -S mem-tracker
 1212  screen -ls
 1213  screen -r compute-session-test
 1214  srun --pty -n 1 -c 2 --time=01:00:00 --gres=gpu:1 --mem=8G bash -l
 1215  squeue -u dwalth
 1216  exit
 1217  ls
 1218  screen -ls
 1219  screen -r mem-tracker 
 1220  screen -ls
 1221  screen -ls
 1222  exit
 1223  nvidia-smi
 1224  nvidia-smils
 1225  ls
 1226  mkdir logs
 1227  cd logs
 1228  ls
 1229  cd ..
 1230  nvidia-smi -f --help
 1231  nvidia-smi --help
 1232  man nvidia-smi
 1233  ls
 1234  git pull
 1235  squeue -u dwalth
 1236  squeue -su dwalth
 1237  squeue -u dwalth -s
 1238  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f logs/nvidia-smi.log
 1239  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f logs/nvidia-smi.log &
 1240  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv
 1241  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 1 --query-gpu=gpu_name,memory.used,memory.free --format=csv
 1242  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv
 1243  bg
 1244  fg
 1245  echo look at the `fg`
 1246  fg
 1247  bg
 1248  fg
 1249  squeue -u dwalth
 1250  squeue -u dwalth -s
 1251  fg
 1252  top
 1253  screen -ls
 1254  screen -ls
 1255  screen -x compute-session-test 
 1256  screen -ls
 1257  screen -r mem-tracker 
 1258  screen -ls
 1259  screen -r mem-tracker 
 1260  screen -r unet-train-1 
 1261  screen -ls
 1262  screen --help
 1263  screen -ls
 1264  screen -S slurm-request-A100-24hrs
 1265  screen -ls
 1266  screen -S mem-connect-test
 1267  screen -ls
 1268  screen -r mem-tracker 
 1269  ls
 1270  screen -ls
 1271  screen -r mem-tracker 
 1272  screen -ls
 1273  screen -r unet-train-1 
 1274  screen -ls
 1275  screen -r slurm-request-A100-24hrs 
 1276  screen -r unet-train-1 
 1277  screen -ls
 1278  ps
 1279  screen -r slurm-request-A100-24hrs 
 1280  screen -ls
 1281  module list
 1282  module load anaconda3
 1283  source activate 3dunet
 1284  cddata/cloud/
 1285  ls
 1286  cd data/cloud/
 1287  ls
 1288  ls
 1289  screen -ls
 1290  cd ~
 1291  squeue --help
 1292  squeue -s -u dwalth
 1293  screen -ls
 1294  srun --pty --jobid 3651555.0 top
 1295  srun --pty --jobid 3651555 top
 1296  srun --pty --jobid 3651555
 1297  srun --pty --jobid 3651555 bash
 1298  srun --pty --jobid 3651555 /bin/bash
 1299  sattach --help
 1300  squeue -s -u dwalth
 1301  sattach  3651555.0
 1302  ls
 1303  screen -ls
 1304  ls
 1305  ps
 1306  squeue -u dwalth
 1307  screen -ls
 1308  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml 
 1309  squeue -u dwalth
 1310  screen -ls
 1311  source activate 3dunet
 1312  ls data/conda/envs/
 1313  module load anaconda3
 1314  source activate 3dunet
 1315  squeue -s -u dwalth
 1316  screen -ls
 1317  bash ~/cloud/pull-script.sh
 1318  ~/cloud
 1319  ls
 1320  bash ~/data/cloud/pull-script.sh  # be sure to pull the newest config files, yamls, etc.
 1321  bash ~/data/cloud/pull-script.sh
 1322  git bash ~/data/cloud/pull-script.shH
 1323  cd data/cloud/
 1324  bash pull-script.sh 
 1325  cd ~
 1326  ls
 1327  bash pull-script.sh 
 1328  git
 1329  cd data/cloud
 1330  bash pull-script.sh 
 1331  git status
 1332  squeue -s -u dwalth
 1333  sattach 3652230.0
 1334  squeue -u dwalth
 1335  sattach 3652230.0
 1336  squeue -u dwalth
 1337  screen -ls
 1338  screen -r unet-train-1 
 1339  screen -ls
 1340  ls -hal
 1341  ls -hal data
 1342  ls -hal /data
 1343  ls -hal data
 1344  ls -hal data/
 1345  ls -hal data/cloud/
 1346  ls -hal data/cloud/chpts/
 1347  date
 1348  time
 1349  man date
 1350  ls -hal data/cloud/chpts/
 1351  mkdir 'test'
 1352  ls
 1353  rm test
 1354  rm -d test
 1355  ls
 1356  cd data/cloud/chpts/
 1357  ls
 1358  date 'chpt-+%y%m%d' | mkdir
 1359  date '+chpt-%y%m%d' | mkdir
 1360  date '+chpt-%y%m%d'
 1361  mkdir date '+chpt-%y%m%d'
 1362  ls
 1363  echo date '+chpt-%y%m%d'
 1364  date '+chpt-%y%m%d' | mkdir
 1365  ls
 1366  mkdir $(date '+chpt-%y%m%d')
 1367  ls
 1368  rm +chpt-%y%m%d/
 1369  rm -d +chpt-%y%m%d
 1370  ls
 1371  enumerate
 1372  ls
 1373  squeue -s -u dwalth
 1374  sattach 3652230.0
 1375  ls
 1376  screen -ls
 1377  squeue -u dwalth
 1378  screen -r slurm-request-A100-24hrs 
 1379  screen -x slurm-request-A100-24hrs 
 1380  screen -S unet
 1381  screen -ls
 1382  screen -r unet 
 1383  screen -r unet ps
 1384  screen --help
 1385  screen -ls
 1386  man scontrol
 1387  scancel --help
 1388  scancel --usage
 1389  squeue -s -u dwalth
 1390  scancel 365223.0
 1391  scancel -u dwalth 3652230.0
 1392  squeue -s -u dwalth
 1393  squeue -s -u dwalth -l 2
 1394  squeue -s -u dwalth -i 2
 1395  squeue -s -u dwalth
 1396  srun --help
 1397  ls
 1398  squeue -s -u dwalth
 1399  sattach 3652230.0
 1400  squeue -s -u dwalth
 1401  sattach 3652230.0
 1402  ls
 1403  ps
 1404  fg
 1405  exit
 1406  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1407  ps
 1408  squeue -u dwalth
 1409  screen -ls
 1410  exit
 1411  screen -ls
 1412  screen -S compute-session-test
 1413  ls
 1414  srun --pty -n 1 -c 2 --time=01:00:00 --gres=gpu:1 --mem=8G bash -l
 1415  fg
 1416  bg
 1417  ps
 1418  nvidia-smi
 1419  top -u dwalth
 1420  ¼Â¨
 1421  exit
 1422  ls
 1423  cd data/cloud
 1424  ls -hal
 1425  bash pull-script.sh 
 1426  nano createDirs.sh
 1427  fg
 1428  ls
 1429  bash pull-script.sh 
 1430  bash commit-script.sh 
 1431  git status
 1432  nano takeArgument.sh
 1433  takeArgument.sh asdf
 1434  bash takeArgument.sh asdf
 1435  bash commit-script.sh 
 1436  nano processArgument.sh
 1437  bash processArgument.sh protocol
 1438  bash processArgument.sh protocols
 1439  bash processArgument.sh 
 1440  bash processArgument.sh @
 1441  nano processArgument.sh
 1442  bash processArgument.sh @
 1443  bash processArgument.sh protocols
 1444  bash processArgument.sh protocols/
 1445  nano processArgument.sh 
 1446  bash processArgument.sh protocols/
 1447  nano processArgument.sh 
 1448  bash processArgument.sh protocols
 1449  bash processArgument.sh README.md
 1450  file README.md 
 1451  nano processArgument.sh 
 1452  file README.md 
 1453  bash processArgument.sh README.md
 1454  mv processArgument.sh processArgumentDir.sh
 1455  cat processArgumentDir.sh 
 1456  bash commit-script.sh 
 1457  nano createDirs.sh 
 1458  nano stringConcatenation.sh
 1459  bash stringConcatenation.sh 
 1460  nano stringConcatenation.sh 
 1461  bash stringConcatenation.sh 
 1462  nano stringConcatenation.sh 
 1463  bash stringConcatenation.sh 
 1464  nano stringConcatenation.sh 
 1465  bash stringConcatenation.sh 
 1466  nano stringConcatenation.sh 
 1467  bash stringConcatenation.sh 
 1468  nano stringConcatenation.sh 
 1469  bash stringConcatenation.sh 
 1470  nano stringConcatenation.sh 
 1471  bash stringConcatenation.sh 
 1472  nano stringConcatenation.sh 
 1473  bash stringConcatenation.sh 
 1474  nano stringConcatenation.sh 
 1475  bash stringConcatenation.sh 
 1476  nano stringConcatenation.sh 
 1477  bash stringConcatenation.sh 
 1478  nano stringConcatenation.sh 
 1479  ls
 1480  ls -l
 1481  ls -t
 1482  ls --help
 1483  ls -C
 1484  ls -F
 1485  lf -lF
 1486  ls -l
 1487  ls -l -F
 1488  find *.sh
 1489  bash commit-script.sh 
 1490  bash processArgumentDir.sh 
 1491  bash processArgumentDir.sh commit-script.sh 
 1492  nano processArgumentDir.sh
 1493  bash processArgumentDir.sh commit-script.sh 
 1494  bash processArgumentDir.sh protocols
 1495  nano processArgumentDir.sh
 1496  bash processArgumentDir.sh protocols
 1497  nano processArgumentDir.sh
 1498  bash processArgumentDir.sh protocols
 1499  nano processArgumentDir.sh
 1500  bash processArgumentDir.sh protocols
 1501  bash processArgumentDir.sh
 1502  nano processArgumentDir.sh
 1503  bash processArgumentDir.sh
 1504  nano processArgumentDir.sh
 1505  bash processArgumentDir.sh
 1506  mkdir chpt-230630-0
 1507  bash processArgumentDir.sh
 1508  rm chpt-230630-0
 1509  rm -d chpt-230630-0
 1510  bash processArgumentDir.sh
 1511  bash processArgumentDir.sh 
 1512  nano processArgumentDir.sh
 1513  bash processArgumentDir.sh 
 1514  nano processArgumentDir.sh
 1515  bash processArgumentDir.sh 
 1516  nano processArgumentDir.sh
 1517  bash processArgumentDir.sh 
 1518  nano processArgumentDir.sh
 1519  bash processArgumentDir.sh 
 1520  nano processArgumentDir.sh
 1521  bash processArgumentDir.sh 
 1522  nano processArgumentDir.sh
 1523  bash processArgumentDir.sh 
 1524  nano processArgumentDir.sh
 1525  bash processArgumentDir.sh 
 1526  nano processArgumentDir.sh
 1527  bash processArgumentDir.sh 
 1528  nano processArgumentDir.sh
 1529  mkdir 'chpt-230630-0'
 1530  bash processArgumentDir.sh 
 1531  nano processArgumentDir.sh
 1532  bash processArgumentDir.sh 
 1533  nano processArgumentDir.sh
 1534  nano fileTest.sh
 1535  cat processArgumentDir.sh
 1536  nano fileTest.sh
 1537  bash fileTest.sh
 1538  cat fileTest.sh
 1539  nano processArgumentDir.sh 
 1540  basnano processArgumentDir.sh 
 1541  bash processArgumentDir.sh 
 1542  rm chpt-230630-0
 1543  rm -d chpt-230630-0
 1544  bash processArgumentDir.sh 
 1545  nano processArgumentDir.sh 
 1546  cat processArgumentDir.sh 
 1547  nano createDirs.sh 
 1548  bash createDirs.sh 
 1549  ls
 1550  bash createDirs.sh 
 1551  ls
 1552  git add .
 1553  git status
 1554  git commit -m "write working directory creating bash script"
 1555  git push
 1556  git status
 1557  squeue -s -u dwalth
 1558  screen -ls
 1559  squeue -u dwalth
 1560  nvidia-smi
 1561  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv
 1562  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230630-0/nvidia-smi.log
 1563  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230630-0/nvidia-smi.log &
 1564  module load anaconda3
 1565  source actiavte 3dunet
 1566  source activate 3dunet
 1567  ls
 1568  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1569  bash data/cloud/pull-script.sh 
 1570  bash ~/data/cloud/pull-script.sh 
 1571  cd ~/data/cloud/
 1572  bash pull-script.sh 
 1573  ls
 1574  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1575  ls
 1576  ls
 1577  ps
 1578  squeue -u dwalth
 1579  screen -ls
 1580  screen -r unet 
 1581  screen -ls
 1582  screen -r slurm-request-A100-24hrs 
 1583  screen -ls
 1584  screen -r mem-tracker 
 1585  screen -ls
 1586  top -u dwalth
 1587  screen -ls
 1588  cd data/cloud/
 1589  ls
 1590  find chpt-2306
 1591  find chpt-2306*
 1592  rm -d chpt-2306*
 1593  find chpt-2306*
 1594  find chpt*
 1595  find -d chpt*
 1596  find --help
 1597  find -D tree chpt
 1598  find -D tree
 1599  find -D tree chpt*
 1600  git status
 1601  git add .
 1602  git status
 1603  bash pull-script.sh 
 1604  ls
 1605  git status
 1606  ls
 1607  find *.sh
 1608  ls -l
 1609  mkdir bashScripts
 1610  mv *.sh bashScripts/
 1611  ls -l *.sh
 1612  ls -l
 1613  find *.md | ls
 1614  find *.md | ls -l
 1615  find *.md
 1616  find *.md | wc -l
 1617  find *.md | ls -l
 1618  ls -l | find *.md
 1619  cd bashScripts/
 1620  ls
 1621  mv pull-script.sh ../
 1622  mv commit-script.sh ../
 1623  nano stringConcatenation.sh 
 1624  bash stringConcatenation.sh 
 1625  nano stringConcatenation.sh 
 1626  bash stringConcatenation.sh 
 1627  nano stringConcatenation.sh 
 1628  bash stringConcatenation.sh 
 1629  nano stringConcatenation.sh 
 1630  bash stringConcatenation.sh 
 1631  nano stringConcatenation.sh 
 1632  bash stringConcatenation.sh 
 1633  ls
 1634  bash createDirs.sh 
 1635  ls
 1636  rm -d chpt-230630-0/
 1637  ls
 1638  mv createDirs.sh ../
 1639  ls
 1640  cd ..
 1641  ls
 1642  find .sh
 1643  find *.sh
 1644  git add .
 1645  git commit -m "clean up shell scripts (bashScripts/ created). leave useful scripts here in main"
 1646  git push
 1647  git status
 1648  ls
 1649  cd chpts
 1650  ls
 1651  ls chpt-230630/
 1652  rm -d chpt-230630/
 1653  ls
 1654  ls date
 1655  rm -r date
 1656  ls
 1657  ls -lha
 1658  cd ..
 1659  ls
 1660  nano createDirs.sh 
 1661  bash createDirs.sh 
 1662  ls
 1663  find chpt*
 1664  find chpt*/
 1665  ls
 1666  ls -l
 1667  ls -l chpts/
 1668  cd chpts/
 1669  cd chpt-230630-0/
 1670  cd ../..
 1671  bash pull-script.sh 
 1672  bash commit-script.sh 
 1673  git status
 1674  screen -ls
 1675  screen -S 3dunet-230630-0
 1676  screen -r 3dunet-230630-0 
 1677  ls
 1678  screen -ls
 1679  ls
 1680  screen -ls
 1681  module load anaconda3
 1682  source activate 3dunet
 1683  cd ~
 1684  ls
 1685  ls data/cloud/pytorch-3dunet/
 1686  ls data/cloud/pytorch-3dunet/resources/
 1687  cd data/cloud/pytorch-3dunet/resources/
 1688  ls
 1689  mv 3DUnet_lightsheet_boundary/ DW-3DUnet_lightsheet_boundary
 1690  ls
 1691  ls -l
 1692  ls DW-3DUnet_lightsheet_boundary/
 1693  cd DW-3DUnet_lightsheet_boundary/
 1694  cd ~/data/cloud
 1695  find train_config.yml
 1696  find */train_config.yml
 1697  bash commit-script.sh 
 1698  train3dunet conda deactivate
 1699  cd ~
 1700  conda deactivate
 1701  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1702  screen -ls
 1703  squeue -s -u dwalth -i 5
 1704  fg
 1705  squeue -u dwalth
 1706  fg
 1707  squeue -u dwalth
 1708  screen -ls
 1709  squeue -u dwalth
 1710  cat data/cloud/chpts/chpt-230630-0/nvidia-smi.log 
 1711  ls
 1712  wc -l vram.txt 
 1713  source activate 3dunet
 1714  conda install torchvision torchaudio
 1715  squeue -s -u dwalth
 1716  screen -ls
 1717  screen -r 3dunet-230630-0 
 1718  exit
 1719  screen -ls
 1720  screen -S 3dunet
 1721  squeue -s -u dwalth
 1722  squeue -s -u dwalth -i 5
 1723  screen -ls
 1724  squeue -s -u dwalth -i 5
 1725  screen -ls
 1726  screen -r 3dunet 
 1727  screen -ls
 1728  squeue -s -u dwalth -i 5
 1729  screen -ls
 1730  squeue -u dwalth
 1731  screen -ls
 1732  squeue -u dwalth
 1733  fg
 1734  screen -ls
 1735  ls
 1736  screen -ls
 1737  squeue -s -u dwalth -i 5
 1738  squeue --help
 1739  squeue -s -u dwalth -i 5
 1740  screen -ls
 1741  squeue -s -u dwalth
 1742  ls
 1743  cd ~
 1744  ls
 1745  ls -hal
 1746  cd home
 1747  ls -lha
 1748  ls -lha dwalth/
 1749  ls -lha dwalth/data/
 1750  ls -lha dwalth/data/wolny/
 1751  ~/home/dwalth
 1752  cd ~
 1753  ls
 1754  pwd
 1755  ls -l
 1756  cd home
 1757  pwd
 1758  ls -lh
 1759  ls -lh ..
 1760  nvidia-smi --list-gpus
 1761  nvidia-smi
 1762  cd ~
 1763  module list
 1764  source actiavte 3dunet
 1765  module load anaconda3
 1766  source activate
 1767  source activate 3dunet
 1768  list
 1769  ls
 1770  cd data/cloud/
 1771  ls
 1772  bash pull-script.sh 
 1773  git status
 1774  ls pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1775  ls chpts/
 1776  ls
 1777  bash pull-script.sh 
 1778  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230703-0/nvidia-smi.log &
 1779  ps
 1780  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-compositeData.yml
 1781  ps
 1782  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-sequenceData.yml
 1783  squeue -u dwalth
 1784  screen -ls
 1785  nvidia-smi
 1786  ps
 1787  bash pull-script.sh 
 1788  git status
 1789  ls chpts/chpt-230703-0/
 1790  cat chpts/chpt-230703-0/
 1791  ps
 1792  ps --help
 1793  man ps
 1794  ps
 1795  ps -p 642730
 1796  ps
 1797  screen -ls
 1798  squeue -u dwalth
 1799  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-sequenceData.yml
 1800  ps
 1801  la
 1802  ls
 1803  ps
 1804  screen -ls
 1805  squeue -s -u dwalth -i 5
 1806  screen -ls
 1807  screen -r 3dunet 
 1808  screen -ls
 1809  squeue -u dwalth
 1810  scancel -u dwalth
 1811  squeue -u dwalth
 1812  screen -ls
 1813  squeue -s -u dwalth
 1814  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230703-0/nvidia-smi.log &
 1815  ps
 1816  squeue -u dwalth
 1817  bash pull
 1818  bash pull-script.sh 
 1819  module load anaconda3
 1820  source activate 3dunet
 1821  ps
 1822  git status
 1823  bash pull-script.sh 
 1824  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1825  bash pull-script.sh 
 1826  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1827  bash pull-script.sh 
 1828  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1829  squeue -u dwalth
 1830  scancel -u dwalth 3770420
 1831  ls
 1832  screen -ls
 1833  screen -r 3dunet 
 1834  screen -ls
 1835  screen -r 3dunet 
 1836  pwd
 1837  source activate 3dunet
 1838  module load anaconda3
 1839  source actiavte
 1840  source activate
 1841  source activate 3dunet
 1842  ls
 1843  pip
 1844  pip install torchvision torchaudio
 1845  ls
 1846  cd data/cloud/
 1847  bash pull-script.sh 
 1848  cd chpts/
 1849  ls
 1850  rm -d chpt-230630-0
 1851  ls chpt-230630-0
 1852  wc -l chpt-230630-0/nvidia-smi.log 
 1853  cat chpt-230630-0/nvidia-smi.log 
 1854  ls
 1855  rm -d -r chpt-230630-0/
 1856  ls
 1857  cd ..
 1858  ls
 1859  bash createDirs.sh 
 1860  nano createDirs.sh 
 1861  git status
 1862  ls
 1863  find proces
 1864  find proces*
 1865  find checkpoint*
 1866  cat processArgument.sh.save 
 1867  rm processArgument.sh.save 
 1868  ls
 1869  git status
 1870  bash commit-script.sh "add message printing the name of the new dir to the console"
 1871  ls
 1872  find chpt*
 1873  find chpt-*
 1874  ls
 1875  ls logs
 1876  wc -l logs/nvidia-smi.log 
 1877  cat logs/nvidia-smi.log 
 1878  ls
 1879  ls chpts/
 1880  ls chpts/chpt-230703-0/
 1881  bash createDirs.sh 
 1882  cd chpts
 1883  ls
 1884  rm chpt-*
 1885  ls
 1886  rm -d chpt-*
 1887  ls
 1888  cd ..
 1889  bash createDirs.sh 
 1890  git status
 1891  bash commit-script.sh 
 1892  cd chpts
 1893  ls
 1894  cd ..
 1895  bash pull-script.sh 
 1896  module load a100
 1897  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1898  module list
 1899  module --help
 1900  module unload a100
 1901  module list
 1902  srun --pty -n 1 -c 4 --gres=gpu --mem=32G --time=03:00:00 bash -l
 1903  ps
 1904  squeue -u dwalth
 1905  module list
 1906  bash pull-script.sh 
 1907  git statu
 1908  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1909  ls
 1910  cat chpts/chpt-230703-0/nv
 1911  cat chpts/chpt-230703-0/nvidia-smi.log 
 1912  wc -l chpts/chpt-230703-0/nvidia-smi.log 
 1913  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230703-0/nvidia-smi.log &
 1914  fg
 1915  ps
 1916  conda deactivate
 1917  screen -ls
 1918  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1919  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1920  squeue -u dwalth
 1921  nvidia-smi
 1922  squeue -s -u dwalth
 1923  nvidia-smi --list-gpus
 1924  module load anaconda3
 1925  source activate 3dunet
 1926  screen -ls
 1927  g
 1928  screen -ls
 1929  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230706-0/nvidia-smi.log &
 1930  ps
 1931  ls
 1932  ls logs/
 1933  ls chpts/
 1934  ls chpts/chpt-230706-0/
 1935  tensorboard --logdir ~/data/cloud/chpts/chpt-230706-0/
 1936  module list
 1937  module load tensorflow
 1938  module load tensorboard
 1939  tensorboard --logdir ~/data/cloud/chpts/chpt-230706-0/
 1940  bash pull
 1941  bash pull-script.sh 
 1942  bash commit-script.sh 
 1943  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1944  bash pull-script.sh 
 1945  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1946  bash pull-script.sh 
 1947  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1948  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml 
 1949  ls
 1950  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1951  git status
 1952  bash pull-script.sh 
 1953  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1954  ls
 1955  ps
 1956  squeue -s -u dwalth
 1957  squeue -u dwalth
 1958  bash pull-script.sh 
 1959  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1960  screen -ls
 1961  cd data/cloud/
 1962  bash pull-script.sh 
 1963  git status
 1964  cd chpts/chpt-230703-0/
 1965  wc -l nvidia-smi.log 
 1966  wc -l logs/
 1967  wc -l logs/events.out.tfevents.1688399020.u20-computegpu-9.643555.0 
 1968  ls logs/
 1969  ls -lha logs
 1970  cd ..
 1971  ls
 1972  cat chpt-230703-0/nvidia-smi.log 
 1973  rm -d chpt-230703-0
 1974  rm -d -r chpt-230703-0
 1975  ls
 1976  cd ..
 1977  bash createDirs.sh 
 1978  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1979  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1980  l
 1981  squeue -u dwalth
 1982  ls
 1983  ls logs/
 1984  wc -l logs/nvidia-smi.log 
 1985  ls -lha logs/
 1986  ls -lha chpts/chpt-230706-0/
 1987  wc -l chpts/chpt-230706-0/nvidia-smi.log 
 1988  cat chpts/chpt-230706-0/nvidia-smi.log 
 1989  screen -ls
 1990  git status
 1991  ls
 1992  screen -ls
 1993  screen -S 3dunet
 1994  screen -ls
 1995  screen -r 3dunet 
 1996  screen -ls
 1997  screen -ls
 1998  squeue -u dwalth
 1999  srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
 2000  squeue -u dwalth
 2001  screen -ls
 2002  history > data/cloud/bash_history-230707.md

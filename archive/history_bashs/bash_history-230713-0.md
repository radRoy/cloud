 1058  cd ~
 1059  ls
 1060  pwd
 1061  ls -l
 1062  cd home
 1063  pwd
 1064  ls -lh
 1065  ls -lh ..
 1066  nvidia-smi --list-gpus
 1067  nvidia-smi
 1068  cd ~
 1069  module list
 1070  source actiavte 3dunet
 1071  module load anaconda3
 1072  source activate
 1073  source activate 3dunet
 1074  list
 1075  ls
 1076  cd data/cloud/
 1077  ls
 1078  bash pull-script.sh 
 1079  git status
 1080  ls pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1081  ls chpts/
 1082  ls
 1083  bash pull-script.sh 
 1084  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230703-0/nvidia-smi.log &
 1085  ps
 1086  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-compositeData.yml
 1087  ps
 1088  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-sequenceData.yml
 1089  squeue -u dwalth
 1090  screen -ls
 1091  nvidia-smi
 1092  ps
 1093  bash pull-script.sh 
 1094  git status
 1095  ls chpts/chpt-230703-0/
 1096  cat chpts/chpt-230703-0/
 1097  ps
 1098  ps --help
 1099  man ps
 1100  ps
 1101  ps -p 642730
 1102  ps
 1103  screen -ls
 1104  squeue -u dwalth
 1105  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-sequenceData.yml
 1106  ps
 1107  la
 1108  ls
 1109  ps
 1110  screen -ls
 1111  squeue -s -u dwalth -i 5
 1112  screen -ls
 1113  screen -r 3dunet 
 1114  screen -ls
 1115  squeue -u dwalth
 1116  scancel -u dwalth
 1117  squeue -u dwalth
 1118  screen -ls
 1119  squeue -s -u dwalth
 1120  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230703-0/nvidia-smi.log &
 1121  ps
 1122  squeue -u dwalth
 1123  bash pull
 1124  bash pull-script.sh 
 1125  module load anaconda3
 1126  source activate 3dunet
 1127  ps
 1128  git status
 1129  bash pull-script.sh 
 1130  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1131  bash pull-script.sh 
 1132  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1133  bash pull-script.sh 
 1134  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1135  squeue -u dwalth
 1136  scancel -u dwalth 3770420
 1137  ls
 1138  screen -ls
 1139  screen -r 3dunet 
 1140  screen -ls
 1141  screen -r 3dunet 
 1142  pwd
 1143  source activate 3dunet
 1144  module load anaconda3
 1145  source actiavte
 1146  source activate
 1147  source activate 3dunet
 1148  ls
 1149  pip
 1150  pip install torchvision torchaudio
 1151  ls
 1152  cd data/cloud/
 1153  bash pull-script.sh 
 1154  cd chpts/
 1155  ls
 1156  rm -d chpt-230630-0
 1157  ls chpt-230630-0
 1158  wc -l chpt-230630-0/nvidia-smi.log 
 1159  cat chpt-230630-0/nvidia-smi.log 
 1160  ls
 1161  rm -d -r chpt-230630-0/
 1162  ls
 1163  cd ..
 1164  ls
 1165  bash createDirs.sh 
 1166  nano createDirs.sh 
 1167  git status
 1168  ls
 1169  find proces
 1170  find proces*
 1171  find checkpoint*
 1172  cat processArgument.sh.save 
 1173  rm processArgument.sh.save 
 1174  ls
 1175  git status
 1176  bash commit-script.sh "add message printing the name of the new dir to the console"
 1177  ls
 1178  find chpt*
 1179  find chpt-*
 1180  ls
 1181  ls logs
 1182  wc -l logs/nvidia-smi.log 
 1183  cat logs/nvidia-smi.log 
 1184  ls
 1185  ls chpts/
 1186  ls chpts/chpt-230703-0/
 1187  bash createDirs.sh 
 1188  cd chpts
 1189  ls
 1190  rm chpt-*
 1191  ls
 1192  rm -d chpt-*
 1193  ls
 1194  cd ..
 1195  bash createDirs.sh 
 1196  git status
 1197  bash commit-script.sh 
 1198  cd chpts
 1199  ls
 1200  cd ..
 1201  bash pull-script.sh 
 1202  module load a100
 1203  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1204  module list
 1205  module --help
 1206  module unload a100
 1207  module list
 1208  srun --pty -n 1 -c 4 --gres=gpu --mem=32G --time=03:00:00 bash -l
 1209  ps
 1210  squeue -u dwalth
 1211  module list
 1212  bash pull-script.sh 
 1213  git statu
 1214  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1215  ls
 1216  cat chpts/chpt-230703-0/nv
 1217  cat chpts/chpt-230703-0/nvidia-smi.log 
 1218  wc -l chpts/chpt-230703-0/nvidia-smi.log 
 1219  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230703-0/nvidia-smi.log &
 1220  fg
 1221  ps
 1222  conda deactivate
 1223  screen -ls
 1224  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1225  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1226  squeue -u dwalth
 1227  nvidia-smi
 1228  squeue -s -u dwalth
 1229  nvidia-smi --list-gpus
 1230  module load anaconda3
 1231  source activate 3dunet
 1232  screen -ls
 1233  g
 1234  screen -ls
 1235  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230706-0/nvidia-smi.log &
 1236  ps
 1237  ls
 1238  ls logs/
 1239  ls chpts/
 1240  ls chpts/chpt-230706-0/
 1241  tensorboard --logdir ~/data/cloud/chpts/chpt-230706-0/
 1242  module list
 1243  module load tensorflow
 1244  module load tensorboard
 1245  tensorboard --logdir ~/data/cloud/chpts/chpt-230706-0/
 1246  bash pull
 1247  bash pull-script.sh 
 1248  bash commit-script.sh 
 1249  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1250  bash pull-script.sh 
 1251  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1252  bash pull-script.sh 
 1253  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1254  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml 
 1255  ls
 1256  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1257  git status
 1258  bash pull-script.sh 
 1259  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1260  ls
 1261  ps
 1262  squeue -s -u dwalth
 1263  squeue -u dwalth
 1264  bash pull-script.sh 
 1265  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1266  screen -ls
 1267  cd data/cloud/
 1268  bash pull-script.sh 
 1269  git status
 1270  cd chpts/chpt-230703-0/
 1271  wc -l nvidia-smi.log 
 1272  wc -l logs/
 1273  wc -l logs/events.out.tfevents.1688399020.u20-computegpu-9.643555.0 
 1274  ls logs/
 1275  ls -lha logs
 1276  cd ..
 1277  ls
 1278  cat chpt-230703-0/nvidia-smi.log 
 1279  rm -d chpt-230703-0
 1280  rm -d -r chpt-230703-0
 1281  ls
 1282  cd ..
 1283  bash createDirs.sh 
 1284  srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
 1285  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1286  l
 1287  squeue -u dwalth
 1288  ls
 1289  ls logs/
 1290  wc -l logs/nvidia-smi.log 
 1291  ls -lha logs/
 1292  ls -lha chpts/chpt-230706-0/
 1293  wc -l chpts/chpt-230706-0/nvidia-smi.log 
 1294  cat chpts/chpt-230706-0/nvidia-smi.log 
 1295  screen -ls
 1296  git status
 1297  ls
 1298  screen -ls
 1299  screen -S 3dunet
 1300  screen -ls
 1301  screen -r 3dunet 
 1302  screen -ls
 1303  screen -ls
 1304  squeue -u dwalth
 1305  screen -ls
 1306  srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
 1307  squeue -u dwalth
 1308  screen -S 3dunet
 1309  screen -ls
 1310  screen -r 3dunet
 1311  screen -ls
 1312  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/nvidia-smi-temp.log &
 1313  ps
 1314  squeue -u dwalth
 1315  squeue -u dwalth -i 2
 1316  ps
 1317  squeue -u dwalth -i 2 &
 1318  ps
 1319  bg
 1320  screen -r 3dunet 
 1321  screen -ls
 1322  screen -S pidKill
 1323  screen -ls
 1324  screen -r pidKill 
 1325  ls
 1326  ps
 1327  squeue -u dwalth -i 1
 1328  ps
 1329  ps -o time
 1330  ps -o etime
 1331  ps -o comm,etime
 1332  ps -o pid,comm,etime
 1333  ps -o pid,comm,etime,time
 1334  ps -o pid,comm,etime
 1335  kill --help
 1336  kill --usage
 1337  kill 1580750
 1338  ps
 1339  ps -o pid,comm,etime
 1340  kill --help
 1341  ps --help
 1342  man ps
 1343  screen -ls
 1344  squeue -u dwalth
 1345  screen -ls
 1346  fg
 1347  ps
 1348  screen -ls
 1349  squeue -s -u dwalth
 1350  nvidia-smi --list-gpus
 1351  module load anaconda3, tensorboard
 1352  module load anaconda3 tensorboard
 1353  module list
 1354  source activate 3dunet
 1355  module list
 1356  ls
 1357  cd data/cloud
 1358  ls
 1359  bash pull-script.sh 
 1360  git status
 1361  bash createDirs.sh 
 1362  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230707-0/nvidia-smi.log &
 1363  ps
 1364  ls chpts/chpt-230706-0/
 1365  ls chpts/chpt-230706-0/logs/
 1366  ls chpts/chpt-230707-0/
 1367  tensorboard --logdir ~/data/cloud/chpts/chpt-230707-0/
 1368  module load tensorboard
 1369  tensorboard --logdir ~/data/cloud/chpts/chpt-230707-0/
 1370  screen -ls
 1371  squeue -u dwalth
 1372  tensorboard --logdir ~/data/cloud/chpts/chpt-230707-0/
 1373  squeue -u dwalth
 1374  nvidia-smi
 1375  ps
 1376  ps --help
 1377  ps
 1378  ls
 1379  bash createDirs.sh 
 1380  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230707-1/nvidia-smi.log &
 1381  ps
 1382  bash pull-script.sh 
 1383  git status
 1384  tensorboard --logdir chpts/chpt-230707-1/
 1385  pip install tensorflow
 1386  module load tensorboard
 1387  module load tensorflow
 1388  tensorboard --logdir chpts/chpt-230707-1/
 1389  bash pull-script.sh 
 1390  ps
 1391  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1392  bash pull-script.sh 
 1393  git status
 1394  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1395  bash pull-script.sh 
 1396  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1397  screen -ls
 1398  ps
 1399  bash createDirs.sh 
 1400  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230707-2/nvidia-smi.log &
 1401  ps
 1402  tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230707-2/
 1403  bash pull-script.sh 
 1404  git status
 1405  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1406  ps
 1407  screen -ls
 1408  screen -ls
 1409  screen -S pidKill
 1410  screen -ls
 1411  squeue -u dwalth
 1412  screen -r 3dunet 
 1413  screen -ls
 1414  srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
 1415  screen -ls
 1416  screen -r 3dunet 
 1417  screen -ls
 1418  cd data/cloud
 1419  ls
 1420  bash createDirs.sh 
 1421  screen -ls  # verify the screen session still exists
 1422  squeue -s -u dwalth  # check thing
 1423  screen -ls
 1424  cd data/cloud
 1425  bash pull-script.sh 
 1426  bash commit-script.sh 
 1427  git status
 1428  screen -S 3dunet230709-0-accum
 1429  screen -ls
 1430  screen -S 3dunet230709-1-405
 1431  scancel -u dwalth 3999613.0
 1432  squeue -u dwalth
 1433  screen -ls
 1434  screen -r 3dunet230709-0-accum 
 1435  ps
 1436  squeue -u dwalth
 1437  nvidia-smi --list-gpus
 1438  squeue -s -u dwalth
 1439  screen -ls
 1440  cd data/cloud/
 1441  ls
 1442  bash pull-script.sh 
 1443  bash commit-script.sh 
 1444  ps
 1445  bash createDirs.sh 
 1446  module load anaconda3 tensorboard
 1447  source activate 3dunet
 1448  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-0/nvidia-smi.log &
 1449  tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-0/
 1450  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1451  bash commit-script.sh 
 1452  git status
 1453  bash pull-script.sh 
 1454  git status
 1455  bash commit-script.sh "add nvidia-smi log"
 1456  git status
 1457  ps
 1458  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1459  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1460  bash pull-script.sh 
 1461  git status
 1462  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1463  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1464  bash pull-script.sh 
 1465  git status
 1466  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1467  ls
 1468  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1469  bash pull-script.sh 
 1470  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1471  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1472  bash pull-script.sh 
 1473  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1474  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1475  bash pull-script.sh 
 1476  git status
 1477  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
 1478  ps
 1479  screen -ls
 1480  srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
 1481  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1482  screen -ls
 1483  squeue -u dwalth
 1484  srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
 1485  ls
 1486  ps
 1487  bash createDirs.sh 
 1488  screen -ls
 1489  squeue -s -u dwalth
 1490  nvidia-smi --list-gpus
 1491  cd ~/data/cloud/
 1492  ls chpts/chpt-230710-0
 1493  cd chpts/chpt-230710-0
 1494  ls
 1495  rm -a -r
 1496  rm -r
 1497  rm --help
 1498  cd ..
 1499  ls
 1500  rm -d chpts/chpt-230710-0/
 1501  rm chpts/chpt-230710-0/*
 1502  rm -d chpts/chpt-230710-0/*
 1503  ls chpts/chpt-230710-0/
 1504  ls chpts/chpt-230710-0/logs
 1505  rm chpts/chpt-230710-0/logs/*
 1506  ls chpts/chpt-230710-0/logs
 1507  ls chpts/chpt-230710-0/
 1508  rm -d chpts/chpt-230710-0/
 1509  rm -d chpts/chpt-230710-0/logs/
 1510  rm -d chpts/chpt-230710-0/H
 1511  ls chpts/
 1512  ls chpts/chpt-230710*
 1513  bash createDirs.sh 
 1514  ls chpts/chpt-230710*
 1515  module load anaconda3 tensorboard
 1516  source activate 3dunet
 1517  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-0/nvidia-smi.log &
 1518  tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-0/
 1519  ps
 1520  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-accumulated.yml
 1521  bash pull-script.sh 
 1522  git status
 1523  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-accumulated.yml
 1524  ps
 1525  ps -o etime
 1526  ps -o etime,comm
 1527  fg
 1528  bg
 1529  bg --help
 1530  ps
 1531  fg
 1532  ps
 1533  ls
 1534  screen -ls
 1535  squeue -u dwalth
 1536  scancel -u dwalth
 1537  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1538  squeue -u dwalth
 1539  screen -ls
 1540  screen -S 3dunet230710-0-405fiji
 1541  screen -ls
 1542  screen -r 3dunet230710-0-405fiji
 1543  screen -ls
 1544  screen -r 3dunet230709-0-accum 
 1545  screen -ls
 1546  screen -S 3dunet-230710-0
 1547  screen -ls
 1548  screen -r 3dunet-
 1549  screen -ls
 1550  screen -S 3dunet-230710-0-accum
 1551  screen -ls
 1552  screen -r 3dunet-230710-0-accum 
 1553  screen -ls
 1554  screen -S 3dunet-230710-1-multichannel
 1555  screen -ls
 1556  screen -r 3dunet-230710-1-multichannel 
 1557  screen -ls
 1558  squeue -u dwalth
 1559  screen -ls
 1560  screen -r 3dunet-230710-1-multichannel 
 1561  screen -ls
 1562  squeue -u dwalth
 1563  squeue -s -u dwalth
 1564  squeue -s -u dwalth
 1565  module load anaconda3 tensorboard
 1566  source activate 3dunet
 1567  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-1/nvidia-smi.log &
 1568  ps
 1569  bash pull-script.sh 
 1570  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-RGB24raw,uint16label-230710-1-3in1out-shapeChange.yml 
 1571  ¼
 1572  ps
 1573  tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-1/
 1574  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-RGB24raw,uint16label-230710-1-3in1out-shapeChange.yml
 1575  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-RGB24raw,uint16label-230710-1-3in1out-shapeChange.yml
 1576  squeue -u dwalth
 1577  bash pull-script.sh 
 1578  git status
 1579  ps
 1580  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-RGB24raw,uint16label-230710-1-3in1out-shapeChange.yml
 1581  bg
 1582  fg
 1583  ps
 1584  scancel -u dwalth
 1585  screen -ls
 1586  cd data/cloud
 1587  ls
 1588  ls chpts/chpt-230710*
 1589  ls chpts/chpt-230710-2
 1590  rm -d chpts/chpt-230710-2
 1591  rm -d chpts/chpt-230710-3
 1592  rm -d chpts/chpt-230710-4
 1593  ls chpts/chpt-230710*
 1594  git status
 1595  bash commit-script.sh 
 1596  screen -ls
 1597  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
 1598  screen -ls
 1599  screen -r 3dunet-230710-1-multichannel 
 1600  screen -ls
 1601  nvidia-smi --list-gpus
 1602  scancel -u dwalth
 1603  screen -S 3dunet-230711-0
 1604  screen -ls
 1605  screen -S 3dunet-230711-1
 1606  screen -r 3dunet-230711-0
 1607  screen -ls
 1608  squeue -u dwalth
 1609  ps
 1610  cd data/cloud/
 1611  git status
 1612  git add .
 1613  git status
 1614  git fetch
 1615  git pull
 1616  git status
 1617  git commit -m "add nvidia log"
 1618  git push
 1619  git status
 1620  bash pull-script.sh 
 1621  git status
 1622  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml 
 1623  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230711-0-lower_patience.yml 
 1624  module list
 1625  module load anaconda3
 1626  source activate 3dunet
 1627  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230711-0/nvidia-smi.log &
 1628  .
 1629  ps
 1630  ls chpts/
 1631  ls chpts/chpt-2307*
 1632  ls chpts/chpt-23071*
 1633  bash createDirs.sh 
 1634  ls chpts/chpt-23071*
 1635  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230711-0/nvidia-smi.log &
 1636  ps
 1637  cat chpts/chpt-230711-0/nvidia-smi.log 
 1638  ps
 1639  fg
 1640  ps
 1641  wc -l chpts/chpt-230711-0/nvidia-smi.log 
 1642  fg
 1643  ps
 1644  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230711-0/nvidia-smi.log &
 1645  ps
 1646  module load tensorboard
 1647  tensorboard --logdir chpts/chpt-230711-0/
 1648  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230711-0-lower_patience.yml
 1649  squeue -u dwalth
 1650  nvidia-smi --list-gpus
 1651  ps
 1652  squeue -s -u dwalth
 1653  nvidia-smi
 1654  scancel -u dwalth
 1655  module load v100-32g
 1656  srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 bash -l
 1657  srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu bash -l
 1658  squeue -u dwalth
 1659  module load v100-16g  # might also work
 1660  module load v100-32g
 1661  srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu bash -l
 1662  squeue -u dwalth
 1663  cd data/cloud/
 1664  bash createDirs.sh 
 1665  screen -ls
 1666  ps
 1667  screen -r 3dunet-230711-0
 1668  screen -ls
 1669  screen -r 3dunet-230711-1 
 1670  screen -ls
 1671  screen -S parent_3dunet
 1672  screen -ls
 1673  screen -r parent_3dunet
 1674  screen -ls
 1675  tmux
 1676  tmux --help
 1677  screen -ls
 1678  screen -r child_3dunet_1
 1679  srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
 1680  squeue -u dwalth
 1681  screen -ls
 1682  history > data/cloud/bash_history-230707.md
 1683  wc -l data/cloud/bash_history-230707.md 
 1684  cd data/cloud
 1685  bash pull-script.sh 
 1686  ps
 1687  bash commit-script.sh 
 1688  git status
 1689  screen -ls
 1690  squeue -u dwalth
 1691  ps
 1692  screen -S child_3dunet_1
 1693  screen -ls
 1694  screen -RR parent_3dunet
 1695  screen -ls
 1696  screen -ls
 1697  screen --help
 1698  screen -ls
 1699  screen -r 3dunet 
 1700  screen -ls
 1701  screen -r parent_3dunet 
 1702  screen -ls
 1703  screen -S 2.1
 1704  screen -ls
 1705  ls
 1706  ps
 1707  screen -S 1
 1708  screen -S 2
 1709  screen -ls
 1710  screen --help
 1711  screen -ls
 1712  screen -wipe 2*
 1713  screen -ls
 1714  screen -wipe
 1715  screen -ls
 1716  screen -wipe 1
 1717  screen -ls
 1718  screen -wipe 2.1
 1719  screen -ls
 1720  screen --help
 1721  screen -x 2.1
 1722  screen -ls
 1723  screen -r 1
 1724  screen -r 2
 1725  screen -ls
 1726  screen -
 1727  screen -ls
 1728  tmux --help
 1729  man tmux
 1730  screen -ls
 1731  tmux -L mux
 1732  tmux -ls
 1733  tmux list-sessions
 1734  tmux -L sesh
 1735  tmux list-sessions
 1736  tmux attach sesh
 1737  screen -ls
 1738  tmux list-sessions
 1739  tmux -L sesh
 1740  tmux list-sessions
 1741  tmux attach sesh
 1742  tmux -L sesh
 1743  tmux attach 1
 1744  tmux attach
 1745  tmux
 1746  tmux -L s1
 1747  tmux
 1748  tmux list-sessions
 1749  tmux attach -t 0
 1750  tmux attach -t 1
 1751  tmux list-session
 1752  tmux attach
 1753  tmux
 1754  tmux list-sessions
 1755  tmux kill-session
 1756  ps --help
 1757  man ps
 1758  screen -S s1
 1759  screen -ls
 1760  nvidia-smi
 1761  srun --pty -n 1 -c 8 --mem=16G --gres=gpu bash -l
 1762  screen -ls
 1763  ls
 1764  squeue -u dwalth -i 3
 1765  screen -ls
 1766  squeue -u dwalth -i 3
 1767  screen -ls
 1768  module list
 1769  screen -ls
 1770  squeue -u dwalth -i 1
 1771  screen -ls
 1772  screen -ls
 1773  tmux list-sessions
 1774  tmux kill-session 1
 1775  tmux kill-session -t 1
 1776  tmux kill-session -t 2
 1777  tmux list-sessions
 1778  tmux
 1779  tmux list-sessions
 1780  tmux kill-session
 1781  tmux list-sessions
 1782  tmux
 1783  tmux list-sessions
 1784  tmux attach 0
 1785  tmux attach -t 0
 1786  tmux list-sessions
 1787  screen -ls
 1788  tmux attach -t 0
 1789  tmux list-sessions
 1790  tmux attach -t 0
 1791  tmux list-sessions
 1792  tmux attach 0
 1793  tmux attach -t 0
 1794  tmux list-sessions
 1795  tmux attach -t 0
 1796  tmux list-sessions
 1797  tmux
 1798  tmux attach -t 0
 1799  tmux attach -t 1
 1800  tmux list-sessions
 1801  tmux attach -t 1
 1802  tmux attach -t 0
 1803  tmux list-sessions
 1804  screen -ls
 1805  screen -ls
 1806  module load anaconda3 tensorboard
 1807  source actiavte 3dunet
 1808  source activate 3dunet
 1809  bash pull-script.sh 
 1810  git status
 1811  nvidia-smi --list-gpus
 1812  tensorboard --logdir ~/data/cloud/chpts/chpt-230712-5-asap/
 1813  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-5-asap/nvidia-smi.log &
 1814  ps
 1815  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-5-patience10,factor0.5,val100,log25.yml
 1816  screen -ls
 1817  squeue -u dwalth
 1818  nvidia-smi --list-gpus
 1819  nvidia-smi
 1820  screen -ls
 1821  bash createDirs.sh 
 1822  mv chpts/chpt-230712-5 chpts/chpt-230712-5-asap
 1823  module list
 1824  screen -ls
 1825  screen -S 3dunet-5-asap
 1826  screen -ls
 1827  screen -r 3dunet-5-asap 
 1828  screen -ls
 1829  screen -r 3dunet-5-asap 
 1830  ps
 1831  squeue -u dwalth
 1832  screen -ls
 1833  screen -r 3dunet-5-asap 
 1834  screen -l
 1835  screen -ls
 1836  screen -r 3dunet-5-asap 
 1837  screen -ls
 1838  screen -ls
 1839  cd data/cloud
 1840  ls
 1841  screen -ls
 1842  srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=12:00:00 bash -l
 1843  tmux list-sessions
 1844  tmux attach -t 1
 1845  tmux list-sessions
 1846  tmux --help
 1847  man tmux
 1848  tmux kill-session -t 1
 1849  tmux list-sessions
 1850  tmux attach -t 0
 1851  tmux list-sessions
 1852  squeue -s -u dwalth
 1853  ls
 1854  ls chpts/chpt-230711-0/
 1855  cd chpts/chpt-230711-0/
 1856  pwd
 1857  screen -ls
 1858  tmux list-sessions
 1859  squeue -u -i 3
 1860  squeue -u dwalth -i 3
 1861  screen -S 3dunet-0
 1862  screen -ls
 1863  screen -r 3dunet-0 
 1864  screen -S 3dunet-1
 1865  screen -ls
 1866  screen -r 3dunet-0
 1867  screen -ls
 1868  screen -r 3dunet-1
 1869  screen -ls
 1870  screen -r 3dunet-0
 1871  screen -ls
 1872  source activate 3dunet
 1873  module load anaconda3 tensorboard
 1874  source activate 3dunet
 1875  screen -r 3dunet-0
 1876  conda deactivate
 1877  screen -r 3dunet-0
 1878  screen -r 3dunet-1 
 1879  screen -ls
 1880  screen -S 3dunet-0
 1881  screen -ls
 1882  screen -r 3dunet-0
 1883  ps
 1884  screen -ls
 1885  screen -r 3dunet-0 
 1886  screen -ls
 1887  cd ~
 1888  screen -ls
 1889  cd data/cloud
 1890  ls
 1891  screen -S 3dunet-1
 1892  screen -ls
 1893  screen -S 3dunet-2
 1894  nvidia-smi
 1895  screen -ls
 1896  screen -S 3dunet-3
 1897  screen -ls
 1898  nvidia-smi
 1899  screen -S 3dunet-4
 1900  screen -ls
 1901  nvidia-smi
 1902  ls
 1903  tmux list-sessions
 1904  screen -ls
 1905  screen -r 3dunet-0
 1906  screen -r 3dunet-4
 1907  screen -ls
 1908  nvidia-smi
 1909  screen -r 3dunet-0
 1910  screen -ls
 1911  nvidia-smi
 1912  screen -r 3dunet-0
 1913  screen -ls
 1914  screen -r 3dunet-1
 1915  screen -r 3dunet-2
 1916  screen -ls
 1917  screen -r 3dunet-3
 1918  screen -ls
 1919  screen -r 3dunet-4
 1920  screen -ls
 1921  tmux list-sessions
 1922  module load anaconda3 tensorboard
 1923  source activate 3dunet
 1924  cd data/cloud/
 1925  ls
 1926  bash pull-script.sh 
 1927  bash createDirs.sh 
 1928  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml 
 1929  cd pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1930  ls
 1931  nano train_config_temp.yml
 1932  cd ~/data/cloud/
 1933  # Sample configuration file for training a 3D U-Net on a task of predicting the boundaries in 3D stack of the Arabidopsis lateral root
 1934  # acquired with the lightsheet microscope. Training done with a combination of Binary Cross-Entropy and DiceLoss.
 1935  # Download training data from: https://osf.io/9x3g2/
 1936  # Download validation data from: https://osf.io/vs6gb/
 1937  # Download test data from: https://osf.io/tn4xj/
 1938  model:
 1939  # loss function to be used during training
 1940  loss:
 1941  optimizer:
 1942  # evaluation metric
 1943  eval_metric:
 1944  lr_scheduler:
 1945  trainer:
 1946  # Configure training and validation loaders
 1947  loaders:
 1948  ps
 1949  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 1950  nvidia-smi
 1951  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv
 1952  bg
 1953  fg
 1954  tmux
 1955  tensorboard --logdir ~/data/cloud/chpts/chpt-230713-0/
 1956  ps
 1957  bg
 1958  fg
 1959  ps
 1960  squeue -s -u dwalth
 1961  nvidia-smi --list-gpus
 1962  nvidia-smi
 1963  screen -ls
 1964  screen -S 3dunet-0
 1965  screen -ls
 1966  squeue -u dwalth
 1967  squeue -s -u dwalth
 1968  screen -ls
 1969  top
 1970  top -u dwalth
 1971  squeue -u dwalth
 1972  scancel 4011147
 1973  cd data/cloud/
 1974  ls
 1975  ls pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config_temp.yml 
 1976  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config_temp.yml 
 1977  ls
 1978  ls pytorch-3dunet/
 1979  ls pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 1980  ls chpts/chpt-23071*
 1981  squeue -s -u dwalth
 1982  screen -ls
 1983  module load tensorboard anaconda3
 1984  ls ~/data/cloud/chpts/chpt-230713-0/
 1985  ls ~/data/cloud/chpts/chpt-230713-2352345/
 1986  tensorboard --logdir ~/data/cloud/chpts/chpt-230713-0/
 1987  ps
 1988  source activate 3dunet
 1989  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230713-0/nvidia-smi.log &
 1990  ps  # verify the nvidia-smi command actually works and is running (= is listed in this command's output)
 1991  nano ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 1992  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 1993  ps
 1994  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 1995  screen -ls
 1996  ps
 1997  nvidia-smi
 1998  screen -ls
 1999  module load tensorboard anaconda3
 2000  source activate 3dunet
 2001  nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230713-0/nvidia-smi.log &
 2002  ps  # verify the nvidia-smi command actually works and is running (= is listed in this command's output)
 2003  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2004  ¼
 2005  cat ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2006  ls
 2007  cd ~
 2008  ls
 2009  ls data/
 2010  cd ~/data/cloud/
 2011  ls
 2012  ls pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 2013  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config_temp.yml 
 2014  screen -ls
 2015  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
 2016  squeue -u dwalth
 2017  ps
 2018  git status
 2019  bash pull-script.sh 
 2020  ps
 2021  tensorboard --logdir ~/data/cloud/chpts/chpt-230713-0/
 2022  bash pull-script.sh 
 2023  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2024  bash pull-script.sh 
 2025  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2026  bash pull-script.sh 
 2027  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2028  bash pull-script.sh 
 2029  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2030  bash pull-script.sh 
 2031  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2032  bash pull-script.sh 
 2033  git add .
 2034  git status
 2035  git add pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/*
 2036  git status
 2037  git commit -m "commit some config files back from cluster"
 2038  git push
 2039  bash pull-script.sh 
 2040  git status
 2041  cat pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 2042  cd pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/
 2043  ls
 2044  \
 2045  ls
 2046  cd named_copies/
 2047  ls
 2048  nano train_config-230713-0-biggerpatch.yml 
 2049  cat train_config-230713-0-biggerpatch.yml 
 2050  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2051  nano train_config-230713-0-biggerpatch.yml 
 2052  train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
 2053  cd ~/data/cloud/
 2054  ls
 2055  ls history_bashs/
 2056  history
 2057  history > history_bashs/bash_history-230713-0.md

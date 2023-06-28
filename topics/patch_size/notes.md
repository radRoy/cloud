# patch size mini-study
daniel walther
creation date: 05.06.2023

This study is about finding out how to specify patch size / shape when training a pytorch-3dunet. Is it possible to make the model not divide into patches to begin with? What are costs & benefits of patch size increase or decrease, respectively? Question like that are intended to be answered, here.

## eralier stuff (search first)

## investigating still open screen session called `tblogdirtest1` from 15.05.23
`2023-05-16 08:18:18,481 [MainThread] INFO UNet3DTrainer - Saving checkpoint to 'home/dwalth/data/wolny/checkpoints/checkpoints_230511-1patch/last_checkpoint.pytorch'`

This was a test about the patch size of input images: Is there only one patch if I specify the patch size to be almost as big as the whole image? The same size gives an error
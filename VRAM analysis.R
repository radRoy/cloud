# VRAM analysis


##### FILE HANDLING #####


# import file (txt)
# library(readr)
# dd_raw <- read_delim("VRAM patch stride table, tab delim.txt", delim = "\t", escape_double = FALSE, trim_ws = TRUE)

# import file (excel)
library(readxl)
X3dunet_session_annotations <- read_excel("cloud/3dunet session annotations.xlsx", 
                                          range = "A1:BA63",
                                          col_types = c("text", "text", "skip", "skip", "skip", "skip", "skip", "skip", "skip", "skip", "skip", "skip", "skip", "skip", "numeric",
                                                        "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text"))
View(X3dunet_session_annotations)
dd_raw <- X3dunet_session_annotations


##### DATA WRANGLING #####


# filter data frame to usable fields
  # valid(usable) session (for VRAM prediction)
    # rename to: valid session
    # use this column for filtering rows (observations)
  # n images
  # n raw channels
  # n label channels
  # bitdepth per raw channel
  # bitdepth per label channel
  # n patches
  # VRAM usage (MiB)
  # VRAM capacity (MiB)
  # res. Z
  # res. Y
  # res. X
  # patch z
  # patch y
  # patch x
colnames(dd_raw)[colnames(dd_raw) == 'valid(usable) session (for VRAM prediction)'] <- 'valid session'
variables <- c('valid session', 'n images', 'n raw channels', 'n label channels', 'bitdepth per raw channel', 'bitdepth per label channel', 'n patches', 'VRAM usage (MiB)', 'VRAM capacity (MiB)', 'res. Z', 'res. Y', 'res. X', 'patch z', 'patch y', 'patch x')
dd <- data.frame(session = dd_raw$session)
for (name in variables) {
  dd[name] <- dd_raw[colnames(dd_raw) == name]
}
#colnames(dd[1]) <- 'valid session'
colnames(dd)
dd <- na.omit(dd)
dd <- dd[dd$`valid session`==1,]


##### ANALYSIS #####


# EDA
dd$patch_volume = dd$`patch z` * dd$`patch y` * dd$`patch x`
plot(dd$`VRAM usage (MiB)` ~ dd$patch_volume)

# SLR
mod <- lm(`VRAM usage (MiB)` ~ patch_volume, data = dd)
summary(mod)
plot(mod)

plot(dd$`VRAM usage (MiB)` ~ dd$patch_volume)
abline(mod)
title("VRAM usage is proportional to the patch volume")

intercept <- mod$coefficients[1]
slope <- mod$coefficients[2]
intercept
slope
# VRAM cap = intercept + patch vol * slope
# patch vol = (VRAM cap - intercept) / slope
patch_vol_max_V100_32 <- (dd$`VRAM capacity (MiB)`[1] - intercept) / slope
paste("patch volume for 80.0 GiB VRAM: ", round(patch_vol_max_V100_32,0), " pixels", sep = "")
  # 14842850 (14.84 MP, 3x16bit raw channels, 1x8bit label channel, with V100's 32 GiB VRAM (not 32 GB as on website))
patch_vol_max_A100_80 <- (76293.9 - intercept) / slope
  # 80.0 GiB = 81920 MiB
paste("patch volume for 80.0 GiB VRAM: ", round(patch_vol_max_A100_80,0), " pixels", sep = "")
  # 35509830 (35.51 MP, 3x16bit raw cahnnels, 1x8bit label channel, with A100's 80 GiB VRAM (not 80 GB as on website))

paste("intercept:", intercept)
paste("slope:", slope)

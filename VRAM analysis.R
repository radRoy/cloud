# VRAM analysis


##### FILE HANDLING #####


# import file
library(readr)
dd_raw <- read_delim("VRAM patch stride table, tab delim.txt", delim = "\t", escape_double = FALSE, trim_ws = TRUE)


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


##### ANALYSIS #####

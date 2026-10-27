library(tidyverse)

setwd("~/RStudioDirectory")
x <- 1:10
my_iris <- iris
my_mtcars <- mtcars

write_csv(my_iris, "my_iris.csv")
saveRDS(x, "x.rds")
y <- readRDS("x.rds")
y
x

save.image("allvariables.Rdata")
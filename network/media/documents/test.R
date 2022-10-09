setwd("C:\\Users/Kudari/OneDrive/Desktop/Testdata")
d <- read.csv("birth.csv")
summary(d)
str(d)
d$edugrp <- as.factor(d$edugrp)
d$occgrp <- as.factor(d$occgrp)
d$reli <- as.factor(d$reli)
d$agegrp <- as.factor(d$agegrp)
d$addgr <- as.factor(d$addgr)
d$parity <- as.factor(d$parity)
d$gender <- as.factor(d$gender)
d$twins <- as.factor(d$twins)
d$fIscal <- ifelse(d$fiscal== 1997 ,1,
                ifelse(d$fiscal == 1998,2,
                       ifelse(d$fiscal == 1999,3,
                              ifelse(d$fiscal == 2000,4,
                                     ifelse(d$fiscal == 2001,5,
                                            ifelse(d$fiscal == 2002,6,
                                                   ifelse(d$fiscal == 2003,7,
                                                          ifelse(d$fiscal == 2004,8,9))))))))
d$fIscal <- as.factor(d$fIscal)
levels(d$fIscal) <- c("1:1997","2:1998","3:1999","4:2000","5:2001","6:2002","7:2003","8:2004","9:2005")
table(d$fIscal)
#Create Fequency table
library(epiDisplay)
tableStack(data = d, vars = c(fIscal,edugrp,occgrp,reli,agegrp,addgr,parity,gender), by=twins)
table(d$twins)
str(d)
attributes(d)
d2 <- subset(d, select = c(3:9,11))
str(d2)
#PCA analysis
options(max.print = 50000) # displayrow
library(caret)
dmy <- dummyVars("~.",data = d2)
trsf <- data.frame(predict(dmy, newdata=d2)) 
pc <- prcomp(trsf, coz=FALSE, score=TRUE)
summary(pc)
str(pc)

d3 <- subset(d, select = c(5:8,10)) # Chisq Selected
m1 <- glm(data =d3,twins~.,family = binomial)
str(d3)
logistic.display(m1)
drop1(m1, test = "Chisq")#Check the model
roc1 <- lroc(m1, title=FALSE,auc.coords = c(.5,.1),graph = TRUE) 
title('ROC of twins(Chisq Test)')
#see the percentage of the area under curve
roc1$auc

d4 <- subset(d, select = c(5:10))#PCA selected
m2 <- glm(data =d4,twins~.,family = binomial)
str(d4)
logistic.display(m2)
roc <- lroc(m2,title =FALSE,auc.coords = c(.5,.1),graph = TRUE)
title('ROC of twins(PCA Test)')
#see the percentage of the area under curve
roc2$auc
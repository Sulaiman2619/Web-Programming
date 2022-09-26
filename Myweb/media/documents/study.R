setwd("C:\\Users/JIB/Desktop/R")

#create a matrix with 3 columns and 2 rows
matrix(1:6, c(2,3))

#create a matrix with the given name of your freinds

age <-c(21,23,21,24,25,26)
nm <- c("Fatah","Arif","Sulaiman","Haiyee","Rahman","Kuddari")

mat1 <- cbind(nm,age)
mat1

mat1[c(1,2),]

#array(data,c(rows,column,dimension))
ar <- array(1:80,c(8,5,2))
ar


d <- read.csv("https://apiradee.sat.psu.ac.th/dexabia.csv")
str(d)
library(datasets)
data()
data(Orange)
str(Orange)

#--------------------------------------------------------------------------------#


library(rvest)

wiki <- read_html("https://wiki.socr.umich.edu/index.php/SOCR_LetterFrequencyData")
html_nodes(wiki, "#content")
englet <- html_table(html_nodes(wiki, "table")[[1]])
str(englet)
getwd()
write.csv(englet, "C:\\Users/JIB/Desktop//R/englet.csv", row.names=FALSE)


db <- read.csv("englet.csv")
db
str(db)

#29062022
#funtion creation

age <- c(45,30,54,38,37)

#average function
avg <- funtion (x) {
  sum(x)/langth(x)
}
avg (age)


ab <- function(a,b,c) {
  (a*b/c)^2
}

ab(30,20,5)


whr = c(0.94,0.81 ,0.87,0.85,0.91,0.78,0.80,0.81,0.85,0.94,1.00 ,0.99 ,0.88 ,0.86 ,0.88)
pcbf= c(38,35,34.4,38, 35.6 ,37.6,29.2,35.7,41.0,36.5,44.7,45.3,36.2,39.3,34.6)

#1 key in these dataset with these two variables of whr and pcbf
m <- cbind(whr,pcbf)

#2 create the id of this dataset

id = c(1:15)

m <- data.frame(id,m)

#3 combine thsese Three variables in to one data frame (id,whr,pobf)

str(m)

#4 call the dataset where id = 10 for pcbf variable only

m[10,3]

#5 call all variables of index number 1 to 5 and 15
m[c(1:5,15),]

#6 call the value of pcbf equal to 38
m[m$pcbf==38,]
subset(m, pcbf == 38)

#7 call the value of whr greather than 95
m[m$whr*100>=95,]



#8 use function of summ() in order to see the basic 
library(epiDisplay)
summ (m)
#9 save this file into r

#10 save the dataset as pcfst.csv
write.csv(m, "C:\\Users/JIB/Desktop//R/pcfst.csv")


#15 August 2022
#probability
#continuous probability distribution
#continuous random variable
#standard normal distribution
std <- seq(-3,3,0.01)
pd <- dnorm(std)
par(mfrow=c(1,2))
plot(std,pd,type = "l", col="blue")
abline(h=seq(0,0.4,0.1),lty="13",col="grey")
abline(v=seq(-3,3,1),lty="13",col="grey")
arrows(x0=-3,y0=0.35,x1=3,y1=0.35,code=3,col='red')
text(x=0,y=0.375,labels='99.26%',col = 'black')
arrows(x0=-2,y0=0.3,x1=2,y1=0.3,code=3,col='red')
text(x=0,y=0.325,labels='95.45%',col = 'black')
arrows(x0=-1,y0=0.25,x1=1,y1=0.25,code=3,col='red')
text(x=0,y=0.275,labels='68.26%%',col = 'black')


plot(std,pd,type = "l", col="blue")

x = c(-3,x,0)
y = c(0,y,0)
polygon(x,y,col = 'red')




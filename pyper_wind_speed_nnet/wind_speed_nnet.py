#import pandas as pd
# 
#import statsmodels.api as sm
# 
#data = pd.read_table('csdata1.txt')
# 
##Y = data.gpa
# 
#X = sm.add_constant(data[['COLLAT1', 'SIZE1', 'PROF2', 'LIQ', 'IND3A']])
# 
## Discrete Dependent Variable Models with Logit Link
# 
#mod = sm.Logit(Y, X)
# 
#res = mod.fit()

import pyper as pr

import numpy as np
 
r = pr.R(use_pandas = True)
 
#r.r_data = data

#r('data <- rbind(r_data, y = 1, wt = r_data$LEV_LT3), cbind(r_data, y = 0, wt = 1 - r_data$LEV_LT3))')


# r('mod <- lm(gpa ~ ., data = data)')



from pyper import *


#outputs = r("x1=seq(1,50, 1); x2=seq(1,100,2); d <- data.frame(x1,x2)")
#print(outputs)

outputs1 = r("library(nnet)")


#r("data1 <- read.table('T6 NWP.txt' )")

#r("data2 <- read.table('T6 EXP.txt' )")

r("indata <- read.table('BMMnnet_input_t6_2013-01-03-06-30:00.txt')")

r("data1<-indata$V8")

r("data2<-indata$V7")

r("rep1=30")

r("nn=240")

r("nn2=384-nn")

r("nn_bootstrap=sample(1:nn, nn,replace=T)")
r("nn1=seq(1:nn);df=cbind(data1,data2);colnames(df)=c('y1','y2');number=rep1*nn2")

r("predict1_out=matrix(seq(1:number), ncol=nn2);number=rep1*nn;predict1_in=matrix(seq(1:number), ncol=nn);cheese1=df[nn_bootstrap,]")

r("nnfit<-nnet(y2~y1, data=cheese1, size=6,skip=F,maxit=50000,decay = 5e-4,linout=TRUE)")

r("data_pred_in=df[nn1,1];\
data_pred_in=data.frame(data_pred_in);\
colnames(data_pred_in)=c('y1');\
y.fit=predict(nnfit, data_pred_in)")


#r("write.table(matrix(y.fit, ncol=length(y.fit)), 'wind prediction in.csv',append = FALSE, sep=',', row.names=FALSE,  col.names=FALSE)")



r("data_pred_out=df[-nn1,1]")

r("data_pred_out=data.frame(data_pred_out)")

r("colnames(data_pred_out)=c('y1')")

# 
# is.data.frame(data_pred_out)

r("y.fit1=predict(nnfit, data_pred_out)")

#r("write.table(matrix(y.fit1, ncol=length(y.fit1)), 'wind prediction_out.csv',append = FALSE, sep=',', row.names=FALSE,  col.names=FALSE)")





r("traininginput <-  as.data.frame(traininginput1)")


r("trainingoutput <- sqrt(traininginput)")

#r('write.table(t(traininginput1), "export1.example.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')




r("numb=1")
r("predict1_in[numb,]=matrix(y.fit, ncol=length(y.fit))")

r("predict1_out[numb,]=matrix(y.fit1, ncol=length(y.fit1))")


r("mm=rep1+5")

r('for (j in (1:5))\
  {for (i in (7:mm))\
  {\
   nn_bootstrap=sample(1:nn, nn);\
   data_train=df[nn_bootstrap,];\
   print (i);\
   nnfit<-nnet(y2~y1, data=data_train, size=i,skip=F,decay = 5e-4,maxit=50000, linout=TRUE);\
   y.fit=predict(nnfit, data_pred_in);\
   y.fit1=predict(nnfit, data_pred_out);\
   numb=i-5;\
   predict1_in[numb,]=matrix(y.fit, ncol=length(y.fit));\
   predict1_out[numb,]=matrix(y.fit1, ncol=length(y.fit1))\
   }\
   }\
   ')

#   write.table(matrix(y.fit1, ncol=length(y.fit1)), "wind prediction_out.csv",append = T, sep=",", row.names=FALSE,  col.names=FALSE);\
#   write.table(matrix(y.fit, ncol=length(y.fit)), "wind prediction in.csv",append = T, sep=",", row.names=FALSE,  col.names=FALSE);\


r("nn1=seq(1:nn); y1_in=x2[1:nn];y1_out=x2[245:384]")

#r("par(mfrow=c(2,2))")

r("pred_ave_in=colMeans(predict1_in)")
r("pred_ave_out=colMeans(predict1_out)")

#r('write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')


r('library(matrixStats)')

r("predict_in_var=colVars(predict1_in)")
r("predict_in_std=colSds(predict1_in)")


r("predict_in_std_high=pred_ave_in +predict_in_std*1.96")

r("predict_in_std_low =pred_ave_in -predict_in_std*1.96")

#r('write.table(matrix(predict_in_std_high, ncol=length(predict_in_std_high)), "wind prediction_in_ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(predict_in_std_low, ncol=length(predict_in_std_low)), "wind prediction_in_ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')



r("predict_out_var=colVars(predict1_out)")
r("predict_out_std=colSds(predict1_out)")


r("predict_out_std_high=pred_ave_out +predict_out_std*1.96")

r("predict_out_std_low=pred_ave_out -predict_out_std*1.96")

#r('write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(predict_out_std_low, ncol=length(predict_out_std_high)), "wind prediction_out_ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r("mean_matrix_in=t(matrix(rep(pred_ave_in, rep1), nrow=nn))")


r("temp=(predict1_in-mean_matrix_in)")

r("P=temp%*%t(temp)+diag(rep1)")



r("library(quadprog)")



r("d=matrix(0, nrow=1, ncol=rep1)")

r("A=diag(rep1)")

r("a1=matrix(1, nrow=rep1)")
r("A=cbind(a1, A)")

r("b=matrix(0, ncol=rep1+1)")
r("b[1]=1")

r("sol = solve.QP (P, -d, A, b,meq=1)")

r("weight=sol$solution")




r("pred_out_ave=weight%*%predict1_out")


r("pred_in_ave=weight%*%predict1_in")

#r('write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(pred_out_ave, ncol=length(pred_out_ave)), "wind prediction_out_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(pred_in_ave, ncol=length(pred_in_ave)), "wind prediction_in_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r("predict_out_matrix=t(matrix(rep(pred_out_ave[1,],rep1),nrow=nn2, ncol=rep1))")

r("predict_out_std=sqrt( weight%*%(predict_out_matrix-predict1_out)^2/(1-sum(weight^2)))")

#r("predict_out_std_high=pred_out_ave[1,] +predict_out_std[1,]*1.96")

#r("predict_out_std_low=pred_out_ave[1,] -predict_out_std[1,]*1.96")

r("predict_out_std_high_w=pred_out_ave[1,] +predict_out_std[1,]*1.96")

r("predict_out_std_low_w=pred_out_ave[1,] -predict_out_std[1,]*1.96")

#r('write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')
#
#r('write.table(matrix(predict_out_std_low, ncol=length(predict_out_std_high)), "wind prediction_out_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(predict_out_std_high_w, ncol=length(predict_out_std_high_w)), "wind prediction_out_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(predict_out_std_low_w, ncol=length(predict_out_std_low_w)), "wind prediction_out_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r("predict_in_matrix=t(matrix(rep(pred_in_ave[1,],rep1),nrow=nn, ncol=rep1))")

r("predict_in_std=sqrt( weight%*%(predict_in_matrix-predict1_in)^2/(1-sum(weight^2)))")


#r("predict_in_std_high=pred_in_ave[1,] +predict_in_std[1,]*1.96")
#
#r("predict_in_std_low=pred_in_ave[1,] -predict_in_std[1,]*1.96")

r("predict_in_std_high_w=pred_in_ave[1,] +predict_in_std[1,]*1.96")

r("predict_in_std_low_w=pred_in_ave[1,] -predict_in_std[1,]*1.96")

#r('write.table(matrix(predict_in_std_high, ncol=length(predict_in_std_high)), "wind prediction_in_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')
#
#r('write.table(matrix(predict_in_std_low, ncol=length(predict_in_std_low)), "wind prediction_in_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(predict_in_std_high_w, ncol=length(predict_in_std_high_w)), "wind prediction_in_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

#r('write.table(matrix(predict_in_std_low_w, ncol=length(predict_in_std_low_w)), "wind prediction_in_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('for (k in 1:nn2)\
    { \
    kk<-k+nn; \
    cat(c(sprintf("%6i %3i %3i %3i %3i %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f \n",indata$V1[kk],indata$V2[kk],indata$V3[kk],indata$V4[kk],indata$V5[kk],indata$V6[kk],indata$V7[kk],indata$V8[kk],pred_ave_out[k],predict_out_std_high[k],predict_out_std_low[k],pred_out_ave[k],predict_out_std_high_w[k],predict_out_std_low_w[k])),file="BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",append=T); \
    }')

r('for (k in 1:nn)\
    { \
    cat(c(sprintf("%6i %3i %3i %3i %3i %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f \n",indata$V1[k],indata$V2[k],indata$V3[k],indata$V4[k],indata$V5[k],indata$V6[k],indata$V7[k],indata$V8[k],pred_ave_in[k],predict_in_std_high[k],predict_in_std_low[k],pred_in_ave[k],predict_in_std_high_w[k],predict_in_std_low_w[k])),file="BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",append=T); \
    }')


##   read and plot ------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages
nn=240

nn2=384-nn

#exp_data = np.loadtxt('T6 EXP.txt')

exp_data = np.loadtxt('BMMnnet_input_t6_2013-01-03-06-30:00.txt',usecols=[6])


pp = PdfPages("BMMnnet_ws_in-sample_pred_t6_2013-01-03-06-30:00.pdf")
plt.figure (0)
plt.clf()
plt.plot(exp_data[0:nn],label="EXP")

exp_in_obs = np.loadtxt('BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv',usecols=[6])

#exp_in_average= np.loadtxt(open("wind prediction_in_ave.csv","rb"),delimiter=",")
exp_in_average= np.loadtxt("BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",usecols=[8])

plt.plot(exp_in_average,color="red", linewidth=1.0, linestyle="-", label="Average")


#exp_in_average_low= np.loadtxt(open("wind prediction_in_ave low.csv","rb"),delimiter=",")
exp_in_average_low= np.loadtxt("BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",usecols=[10])

#exp_in_average_high= np.loadtxt(open("wind prediction_in_ave high.csv","rb"),delimiter=",")
exp_in_average_high= np.loadtxt("BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",usecols=[9])

plt.plot(exp_in_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_in_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))
#plt.ylim(min(np.concatenate((exp_data[0:nn],exp_in_average_low), axis=1))-0.5, max(np.concatenate((exp_data[0:nn],exp_in_average_high), axis=1))+0.5)
plt.ylim(min(np.concatenate((exp_in_obs,exp_in_average_low), axis=1))-0.5, max(np.concatenate((exp_in_obs,exp_in_average_high), axis=1))+0.5)

plt.xlim(1,nn)

plt.legend(loc='upper right')

plt.ylabel('Wind speed', fontsize=14)
plt.xlabel('Hour', fontsize=14)

plt.title('In-sample equal weight prediction', fontsize=22)

pp.savefig()
pp.close()


pp = PdfPages("BMMnnet_ws_out-sample_pred_t6_2013-01-03-06-30:00.pdf")
plt.figure (1)
plt.clf()

#exp_out_average= np.loadtxt(open("wind prediction_out_ave.csv","rb"),delimiter=",")
#exp_out_average_low= np.loadtxt(open("wind prediction_out_ave low.csv","rb"),delimiter=",")
#exp_out_average_high= np.loadtxt(open("wind prediction_out_ave high.csv","rb"),delimiter=",")

exp_out_average= np.loadtxt("BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",usecols=[8])
exp_out_average_low= np.loadtxt("BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",usecols=[10])
exp_out_average_high= np.loadtxt("BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",usecols=[9])
exp_out_obs = np.loadtxt('BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv',usecols=[6])

#plt.plot(exp_data[(nn+1):384],label="EXP")
plt.plot(exp_out_obs,label="EXP")

#plt.ylim(min(np.concatenate((exp_data[(nn+1):384],exp_in_average_low), axis=1))-0.50, max(np.concatenate((exp_data[(nn+1):384],exp_in_average_high), axis=1))+0.50)
plt.ylim(min(np.concatenate((exp_out_obs,exp_out_average_low), axis=1))-0.50, max(np.concatenate((exp_out_obs,exp_out_average_high), axis=1))+0.50)

plt.xlim(1,nn2)

plt.plot(exp_out_average,color="red", linewidth=1.0, linestyle="-", label="Average")

plt.plot(exp_out_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_out_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))

plt.legend(loc='upper left')

plt.ylabel('Wind speed', fontsize=14)
plt.xlabel('Hour', fontsize=14)

plt.title('Out-of-sample equal weight prediction', fontsize=22)
pp.savefig()
pp.close()


pp = PdfPages("BMMnnet_ws_in-sample_wgt_pred_t6_2013-01-03-06-30:00.pdf")
plt.figure (2)
plt.clf()
#plt.plot(exp_data[0:nn],label="EXP")
plt.plot(exp_in_obs,label="EXP")

#exp_in_average= np.loadtxt(open("wind prediction_in_weight ave.csv","rb"),delimiter=",")
#exp_in_average_low= np.loadtxt(open("wind prediction_in_weight ave low.csv","rb"),delimiter=",")
#exp_in_average_high= np.loadtxt(open("wind prediction_in_weight ave high.csv","rb"),delimiter=",")

exp_in_average= np.loadtxt("BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",usecols=[11])
exp_in_average_low= np.loadtxt("BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",usecols=[13])
exp_in_average_high= np.loadtxt("BMMnnet_output_in-sample_t6_2013-01-03-06-30:00.csv",usecols=[12])

plt.plot(exp_in_average,color="red", linewidth=1.0, linestyle="-", label="Average")

plt.plot(exp_in_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_in_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))
#plt.ylim(min(np.concatenate((exp_data[0:nn],exp_in_average_low), axis=1))-0.50, max(np.concatenate((exp_data[0:nn],exp_in_average_high), axis=1))+0.50)
plt.ylim(min(np.concatenate((exp_in_obs,exp_in_average_low), axis=1))-0.50, max(np.concatenate((exp_in_obs,exp_in_average_high), axis=1))+0.50)



plt.xlim(1,nn)

plt.legend(loc='upper right')

plt.title('In-sample weighted prediction', fontsize=22)
plt.ylabel('Wind speed', fontsize=14)
plt.xlabel('Hour', fontsize=14)
pp.savefig()
pp.close()


pp = PdfPages("BMMnnet_ws_out-sample_wgt_pred_t6_2013-01-03-06-30:00.pdf")
plt.figure (3)
plt.clf()
#plt.plot(exp_data[(nn+1):384],label="EXP")
plt.plot(exp_out_obs,label="EXP")

#exp_out_average= np.loadtxt(open("wind prediction_out_weight ave.csv","rb"),delimiter=",")
#exp_out_average_low= np.loadtxt(open("wind prediction_out_weight ave low.csv","rb"),delimiter=",")
#exp_out_average_high= np.loadtxt(open("wind prediction_out_weight ave high.csv","rb"),delimiter=",")

exp_out_average= np.loadtxt("BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",usecols=[11])
exp_out_average_low= np.loadtxt("BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",usecols=[13])
exp_out_average_high= np.loadtxt("BMMnnet_output_out-sample_t6_2013-01-03-06-30:00.csv",usecols=[12])

#plt.ylim(min(np.concatenate((exp_data[(nn+1):384],exp_in_average_low), axis=1))-0.50, max(np.concatenate((exp_data[(nn+1):384],exp_in_average_high), axis=1))+0.50)
plt.ylim(min(np.concatenate((exp_out_obs,exp_out_average_low), axis=1))-0.50, max(np.concatenate((exp_out_obs,exp_out_average_high), axis=1))+0.50)

plt.xlim(1,nn2)

plt.plot(exp_out_average,color="red", linewidth=1.0, linestyle="-", label="Average")

plt.plot(exp_out_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_out_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))

plt.legend(loc='upper left')

plt.title('Out-of-sample equal weighted prediction', fontsize=22)

plt.ylabel('Wind speed', fontsize=14)
plt.xlabel('Hour', fontsize=14)

pp.savefig()
pp.close()

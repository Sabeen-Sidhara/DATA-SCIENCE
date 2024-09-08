import pandas as pd
import numpy as np
class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for ColumnName in dataset.columns:

            if (dataset[ColumnName].dtype=='O'):
                qual.append(ColumnName)
            else:
                 quan.append(ColumnName)
        return quan,qual

    def UniVariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:99%","Q5:100%","IQR","1.5Rule","Lesser","Greater","Minimum","Maximum","skew",'kurtosis','var','std'],columns=quan)
        for ColumnName in quan:
            descriptive[ColumnName]["Mean"]=dataset[ColumnName].mean()
            descriptive[ColumnName]["Median"]=dataset[ColumnName].median()
            descriptive[ColumnName]["Mode"]=dataset[ColumnName].mode()[0]
            descriptive[ColumnName]["Q1:25%"]=dataset.describe()[ColumnName]["25%"]
            descriptive[ColumnName]["Q2:50%"]=dataset.describe()[ColumnName]["50%"]
            descriptive[ColumnName]["Q3:75%"]=dataset.describe()[ColumnName]["75%"]
            descriptive[ColumnName]["Q4:99%"]=np.percentile(dataset[ColumnName],99)
            descriptive[ColumnName]["Q5:100%"]=dataset.describe()[ColumnName]["max"]
            descriptive[ColumnName]["IQR"]= descriptive[ColumnName]["Q3:75%"]-descriptive[ColumnName]["Q1:25%"]
            descriptive[ColumnName]["1.5Rule"]=1.5*descriptive[ColumnName]["IQR"]
            descriptive[ColumnName]["Lesser"]=descriptive[ColumnName]["Q1:25%"]-descriptive[ColumnName]["1.5Rule"]
            descriptive[ColumnName]["Greater"]=descriptive[ColumnName]["Q3:75%"]+descriptive[ColumnName]["1.5Rule"]
            descriptive[ColumnName]["Minimum"]=dataset[ColumnName].min()
            descriptive[ColumnName]["Maximum"]=dataset[ColumnName].max()
            descriptive[ColumnName]["skew"]=dataset[ColumnName].skew()
            descriptive[ColumnName]["kurtosis"]=dataset[ColumnName].kurtosis()
            descriptive[ColumnName]["var"]=dataset[ColumnName].var()
            descriptive[ColumnName]["std"]=dataset[ColumnName].std()
        return descriptive

    def FindingOutlier(quan, descriptive):
        Lesser = []
        Greater = []
        for ColumnName in quan:
            if descriptive[ColumnName]["Minimum"] < descriptive[ColumnName]["Lesser"]:
                Lesser.append(ColumnName)
                if descriptive[ColumnName]["Maximum"] > descriptive[ColumnName]["Greater"]:
                    Greater.append(ColumnName)
        return Lesser, Greater
    
    def ReplacingOutliers(dataset, descriptive, quan, Lesser, Greater):
        for ColumnName in Lesser:
            dataset[ColumnName][dataset[ColumnName]<descriptive[ColumnName]["Lesser"]]=descriptive[ColumnName]["Lesser"]
        for ColumnName in Greater:
            dataset[ColumnName][dataset[ColumnName]>descriptive[ColumnName]["Greater"]]=descriptive[ColumnName]["Greater"]
            return dataset

    def FreqTable(ColumnName, dataset):
        FreqTable = pd.DataFrame(columns=["Unique_Values", "Frequency", "Relative_Frequency", "cumsum"])
        FreqTable["Unique_Values"] = dataset[ColumnName].value_counts().index
        FreqTable["Frequency"] = dataset[ColumnName].value_counts().values
        FreqTable["Relative_Frequency"] = FreqTable["Frequency"] / len(dataset)
        FreqTable[ "cumsum"] = FreqTable["Relative_Frequency"].cumsum()
        return FreqTable
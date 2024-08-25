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
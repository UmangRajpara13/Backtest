import GlobVar

# Selling STOCKS
def Pinbar(self):

    maxhigh = self.high
    n = 0
    if ((self.open < (((self.high - self.low) * 0.5) + self.low)) 
        & (self.close < (((self.high - self.low) * 0.5) + self.low)) 
        & (self.open > self.close) & (self.close * 0.99 < self.nextopen < self.close * 1.01)):
            
        for j in range(self.i - 10, self.i):
            dailyhigh = float(self.data[j][5])

            if (maxhigh > dailyhigh):
                n += 1;
                if (n == 10):
                    
                    closediff = ((self.nextclose - self.close) * 100) / self.close
                    
                    if (self.tgtper >= 0.5):

                        GlobVar.RESULT.insert(GlobVar.count, ["",self.date, self.PevDlypercent, self.tgtper, closediff,"Profit"])
                        GlobVar.totalwin += 1
                        GlobVar.count +=1
                        GlobVar.tradecount += 1
                        GlobVar.points = GlobVar.points + (self.nextopen * 0.5 / 100)

                    else:

                        GlobVar.RESULT.insert(GlobVar.count, ["",self.date, self.PevDlypercent, self.tgtper, closediff,"Loss"])
                        GlobVar.totallose += 1
                        GlobVar.count +=1
                        GlobVar.tradecount += 1
                        GlobVar.points = GlobVar.points - (self.nextopen - self.nextclose)
            else:
                break
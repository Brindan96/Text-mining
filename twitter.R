
# Extracting tweets from twitter
# I didnt get Twitter Api account, its still in review but kindly see the code and tell if any mistakes are there 
library("twitteR")
install.packages("ROAuth")
library("ROAuth")

cred <- OAuthFactory$new(consumerKey='', # Consumer Key (API Key)
                         consumerSecret='', #Consumer Secret (API Secret)
                         requestURL='https://api.twitter.com/oauth/request_token',
                         accessURL='https://api.twitter.com/oauth/access_token',
                         authURL='https://api.twitter.com/oauth/authorize')

save(cred, file="twitter authentication.Rdata")

load("twitter authentication.Rdata")

install.packages("base64enc")
library(base64enc)

install.packages("httpuv")
library(httpuv)

setup_twitter_oauth("", # Consumer Key (API Key)
                    "", #Consumer Secret (API Secret)
                    "",  # Access Token
                    "")  #Access Token Secret



Tweets <- userTimeline('TheRock', n = 1000,includeRts = T)
TweetsDF <- twListToDF(Tweets)
dim(TweetsDF)
View(TweetsDF)

write.csv(TweetsDF, "Tweets.csv",row.names = F)

getwd()

handleTweets <- searchTwitter('Cristiano', n = 10000)


# Emotion Mining

install.packages("syuzhet")
library("syuzhet")

s_v <- get_sentences(handleTweets)
class(s_v)
str(s_v)
head(s_v)

sentiment_vector <- get_sentiment(s_v, method = "bing")
head(sentiment_vector)

afinn_s_v <- get_sentiment(s_v, method = "afinn")
head(afinn_s_v)

nrc_vector <- get_sentiment(s_v, method="nrc")
head(nrc_vector)

sum(sentiment_vector)
mean(sentiment_vector)
summary(sentiment_vector)

# plot
plot(sentiment_vector, type = "l", main = "Plot Trajectory",
     xlab = "Narrative Time", ylab = "Emotional Valence")
abline(h = 0, col = "red")











# extracting reviews

library(rvest)
install.packages("XML")
library(XML)
install.packages("magrittr")
library(magrittr)

# Amazon Reviews 
aurl <- "https://www.amazon.in/Mi-Inches-Full-Android-Black/product-reviews/B07T89Z35Z/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber="
amazon_reviews <- NULL
for (i in 1:200){
  murl <- read_html(as.character(paste(aurl,i,sep="")))
  rev <- murl %>%
    html_nodes(".review-text") %>%
    html_text()
  amazon_reviews <- c(amazon_reviews,rev)
}
amazon_review=write.table(amazon_reviews,"bluetoothspeaker01.txt",row.names=FALSE)


# Emotion Mining

install.packages("syuzhet")
library("syuzhet")

s_v <- get_sentences(amazon_review)
class(s_v)
str(s_v)
head(s_v)

sentiment_vector <- get_sentiment(s_v, method = "bing")
head(sentiment_vector)

afinn_s_v <- get_sentiment(s_v, method = "afinn")
head(afinn_s_v)

nrc_vector <- get_sentiment(s_v, method="nrc")
head(nrc_vector)

sum(sentiment_vector)
mean(sentiment_vector)
summary(sentiment_vector)

# plot
plot(sentiment_vector, type = "l", main = "Plot Trajectory",
     xlab = "Narrative Time", ylab = "Emotional Valence")
abline(h = 0, col = "red")






# Snapdeal reviews 
surl_1 <- "https://www.snapdeal.com/product/apple-iphone-6s-32gb-space/647328495952/reviews?page="
surl_2 <- "&sortBy=HELPFUL#defRevPDP"
snapdeal_reviews <- NULL
for (i in 1:70){
  surl <- read_html(as.character(paste(surl_1,surl_2,sep=as.character(i))))
  srev <- surl %>%
    html_nodes("#defaultReviewsCard p") %>%
    html_text()
  snapdeal_reviews <- c(snapdeal_reviews,srev)
}

snapdeal_review=write.table(snapdeal_reviews,"samsung01.txt")



install.packages("syuzhet")
library("syuzhet")

s_v <- get_sentences(snapdeal_review)
class(s_v)
str(s_v)
head(s_v)

sentiment_vector <- get_sentiment(s_v, method = "bing")
head(sentiment_vector)

afinn_s_v <- get_sentiment(s_v, method = "afinn")
head(afinn_s_v)

nrc_vector <- get_sentiment(s_v, method="nrc")
head(nrc_vector)

sum(sentiment_vector)
mean(sentiment_vector)
summary(sentiment_vector)

# plot
plot(sentiment_vector, type = "l", main = "Plot Trajectory",
     xlab = "Narrative Time", ylab = "Emotional Valence")
abline(h = 0, col = "red")





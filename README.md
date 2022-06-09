# pr-api 
## An application to test PR activity over the last 7 days.   This application could use some security modifications but at this time, it is setup to just simply print to STDOUT

## Running
# Simply clone the repo, build the docker image and run the container.   It should be very straight forward.   Once I am inside of a fw with a trusted smtp server I can get the email functionality working!

## Testing
I tested this application with a slower and busier repo with and without pagination and got it working. 


## Test Results

subject: Report for open/closed pull request over the last week for repo argo-cd 


PR             Date Created                  Status
9626           2022-06-09T16:15:10Z          open 
9625           2022-06-09T15:25:27Z          open 
9624           2022-06-09T13:43:30Z          open 
9623           2022-06-09T13:01:04Z          open 
9622           2022-06-09T10:09:59Z          open 
9620           2022-06-09T03:14:41Z          open 
9619           2022-06-08T21:22:36Z          open 
9618           2022-06-08T20:33:39Z          closed
9617           2022-06-08T20:03:50Z          closed
9616           2022-06-08T19:57:16Z          open 
9615           2022-06-08T19:51:43Z          open 
9614           2022-06-08T19:03:13Z          closed
9613           2022-06-08T17:19:47Z          open 
9612           2022-06-08T15:49:53Z          open 
9611           2022-06-08T15:30:56Z          closed
9610           2022-06-08T15:29:25Z          open 
9609           2022-06-08T10:38:28Z          open 
9608           2022-06-08T10:29:44Z          open 
9607           2022-06-08T09:33:00Z          open 
9606           2022-06-08T07:27:53Z          open 
9605           2022-06-08T02:59:53Z          open 
9604           2022-06-08T02:57:10Z          open 
9603           2022-06-08T00:30:02Z          open 
9602           2022-06-07T20:16:04Z          open 
9601           2022-06-07T20:11:21Z          open 
9600           2022-06-07T16:38:15Z          closed
9599           2022-06-07T16:15:39Z          open 
9598           2022-06-07T15:40:14Z          open 
9597           2022-06-07T14:25:19Z          open 
9596           2022-06-07T13:54:09Z          open 
9595           2022-06-07T08:27:56Z          open 
9594           2022-06-07T05:58:18Z          open 
9593           2022-06-07T00:58:12Z          open 
9592           2022-06-06T23:18:51Z          open 
9591           2022-06-06T21:59:21Z          open 
9590           2022-06-06T21:36:24Z          closed
9589           2022-06-06T19:41:06Z          open 
9588           2022-06-06T17:28:10Z          open 
9587           2022-06-06T15:04:53Z          open 
9585           2022-06-06T12:19:19Z          closed
9584           2022-06-05T19:09:46Z          open 
9583           2022-06-05T13:04:58Z          closed
9582           2022-06-05T06:08:18Z          open 
9581           2022-06-04T13:26:16Z          open 
9580           2022-06-04T11:51:31Z          open 
9579           2022-06-04T07:18:37Z          open 
9577           2022-06-03T14:55:08Z          closed
9575           2022-06-03T08:17:14Z          open 
9574           2022-06-03T07:54:18Z          open 
9573           2022-06-03T07:32:21Z          open 
9572           2022-06-02T20:22:20Z          open 
9571           2022-06-02T20:15:56Z          open 
9570           2022-06-02T14:18:48Z          open 
9569           2022-06-02T14:11:02Z          open 
9568           2022-06-02T12:15:17Z          open 
9567           2022-06-02T08:57:27Z          closed
9566           2022-06-02T02:55:03Z          closed
9565           2022-06-02T02:53:56Z          closed
9563           2022-06-01T23:30:35Z          closed
9562           2022-06-01T22:20:42Z          open 
9561           2022-06-01T22:17:55Z          closed
9559           2022-06-01T20:26:51Z          closed
9558           2022-06-01T19:46:00Z          open 
9557           2022-06-01T17:20:53Z          closed
9556           2022-06-01T16:09:40Z          open 
9552           2022-06-01T12:45:20Z          open 
9551           2022-06-01T07:58:48Z          closed
9548           2022-05-31T20:43:33Z          closed
9547           2022-05-31T16:35:16Z          closed
9546           2022-05-31T15:55:49Z          closed
9543           2022-05-31T11:34:56Z          open 
9540           2022-05-30T16:58:40Z          closed
9539           2022-05-30T16:57:42Z          closed
9534           2022-05-28T10:00:42Z          closed
9529           2022-05-27T13:30:36Z          closed
9527           2022-05-27T11:30:10Z          open 
9524           2022-05-26T23:23:56Z          open 
9514           2022-05-25T18:25:23Z          closed
9513           2022-05-25T18:13:49Z          closed
9496           2022-05-24T04:25:23Z          open 
9478           2022-05-22T01:48:40Z          open 
9464           2022-05-20T13:15:37Z          open 
9462           2022-05-20T10:37:07Z          closed
9461           2022-05-20T10:34:04Z          closed
9437           2022-05-17T21:32:56Z          open 
9422           2022-05-16T16:36:55Z          closed
9419           2022-05-16T13:03:41Z          closed
9417           2022-05-16T09:17:53Z          closed
9413           2022-05-15T03:47:48Z          open 
9405           2022-05-13T16:26:34Z          open 
9391           2022-05-13T03:35:55Z          closed
9387           2022-05-12T18:28:33Z          closed
9374           2022-05-11T21:34:35Z          closed
9363           2022-05-11T16:01:27Z          closed
9335           2022-05-09T13:55:47Z          closed
9319           2022-05-06T14:25:21Z          closed
9312           2022-05-05T20:43:54Z          open 
9300           2022-05-04T15:55:09Z          closed
9283           2022-05-03T11:34:37Z          open 
9276           2022-05-02T19:24:46Z          open 
9272           2022-05-02T11:11:36Z          closed
9254           2022-04-29T13:17:11Z          open 
9190           2022-04-24T03:38:32Z          closed
9175           2022-04-22T08:40:25Z          closed
9167           2022-04-21T19:20:34Z          closed
9145           2022-04-19T19:53:47Z          open 
9135           2022-04-18T15:48:32Z          open 
9123           2022-04-17T07:46:10Z          open 
9080           2022-04-12T17:54:20Z          closed
9077           2022-04-12T14:40:18Z          open 
9070           2022-04-11T18:54:36Z          open 
9069           2022-04-11T18:43:05Z          open 
9040           2022-04-08T05:43:40Z          open 
9015           2022-04-06T11:31:04Z          open 
8986           2022-04-04T14:10:59Z          closed
8938           2022-03-30T12:51:23Z          open 
8904           2022-03-25T22:45:05Z          closed
8822           2022-03-18T14:17:22Z          closed
8812           2022-03-17T13:39:17Z          closed
8808           2022-03-17T09:24:41Z          closed
8755           2022-03-11T08:02:48Z          closed
8731           2022-03-09T10:58:24Z          open 
8698           2022-03-07T14:26:35Z          open 
8683           2022-03-04T14:42:42Z          open 
8680           2022-03-04T13:39:08Z          open 
8665           2022-03-03T15:06:44Z          open 
8497           2022-02-14T22:09:34Z          open 
8413           2022-02-07T16:48:10Z          closed
8394           2022-02-05T12:00:00Z          open 
8340           2022-02-02T04:25:47Z          open 
8329           2022-02-01T13:32:37Z          closed
8141           2022-01-11T09:53:47Z          open 
8117           2022-01-07T19:42:00Z          open 
8067           2021-12-30T19:19:25Z          open 
7995           2021-12-20T04:17:39Z          open 
7992           2021-12-19T11:20:12Z          open 
7957           2021-12-16T13:50:15Z          open 
7927           2021-12-14T17:26:41Z          open 
7799           2021-11-29T19:13:06Z          open 
7752           2021-11-19T06:32:53Z          open 
7534           2021-10-23T08:04:22Z          open 
7437           2021-10-14T07:28:34Z          open 
7436           2021-10-14T07:25:13Z          closed
7426           2021-10-13T14:13:35Z          open 
7352           2021-10-04T00:25:02Z          open 
7089           2021-08-26T09:13:02Z          open 
6303           2021-05-23T15:46:26Z          open 
6228           2021-05-12T23:58:49Z          open 
6125           2021-04-29T08:25:53Z          open 
6110           2021-04-27T08:33:14Z          open 
6086           2021-04-22T11:30:13Z          open 
6055           2021-04-19T08:56:58Z          open 
5456           2021-02-08T17:49:17Z          open 
5107           2020-12-22T08:40:23Z          open 
4979           2020-12-05T03:41:37Z          open 
4863           2020-11-19T12:45:54Z          closed
4639           2020-10-22T08:16:12Z          closed
4358           2020-09-16T23:16:18Z          closed
4204           2020-08-29T11:08:37Z          closed
4071           2020-08-11T12:53:13Z          open 
3709           2020-06-04T09:08:26Z          open 
3583           2020-05-13T14:19:38Z          open 
3280           2020-03-25T04:57:06Z          closed
2789           2019-12-02T16:10:27Z          open 
2638           2019-11-05T11:16:33Z          open 
2424           2019-10-07T13:14:46Z          open 
998            2019-01-09T22:21:36Z          closed

subject: Report for open/closed pull request over the last week for repo pygithub 


PR             Date Created                  Status
2251           2022-06-07T13:59:25Z          closed
2250           2022-06-06T14:35:57Z          closed
1293           2019-11-20T14:06:52Z          closed

# DOCKER Testing


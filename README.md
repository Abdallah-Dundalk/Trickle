# Trickle
Business Model
This is a web application which can be accessed through a browser and is intended to be used by music lovers with Rap/ Hip hop being the predominant genre of music being catered for. This application allows consumers to listen to music by streaming the music to a front end music player.
This application gives the user access to a catalogue of music and the ability to organise their favourite tracks into playlists that they can create and edit . Given that the music is streamed and played via the app, there is no need for downloading or installing any software, except for a web browser, of course. While initially it may seem that catering for one genre of music may limit the consumer base, raps influnce on modern culture is vast and is therfore not  a niche market.
By focusing on content that is more 'underground' , and providing the service at a more affordable cost, the aim is to find an opportunity in a market that is dominated by larger more established services by, attracting consumers who are looking for the hidden gems in artists that are not yet widely known. Trickle is for people who want original music thats not so main stream.
Trickle offers two options for cunsumers. Option 1 is 90 days access for 8 euro. Option 2 is 1 year for 20 euro. this is far cheaper than most streaming services.

# Marketing Strategy:
Social media will be the primary means of marketing for Trickle initially, given that Facebook provides the ability to share content and reach potentially huges audience for little cost, it makes perfect sense to use it as a marketing platform. Facebook lends itself well for businesses like Trickle as the product we provide can be share easily creating brand awareness along the way. Trickles goal is to place the product where the audience can easily find it and share it. 
The 2nd aspect of Trickles marketing comprises of mail marketing. By providing a news letter sign up option on the app, we can keep customers engaged by keeping them informed of products beign offered or updates to services provided or even offering discounts for reffering new members.

The web application can be accessed here - https://trickle.herokuapp.com/

![Trickle Landing Page]( /media/home_page.JPG)

## Existing Features:
Landing Page:
Here the user is met with a carousel that quickly explains the application's purpose while using images that convey passion, fun and a bit of 'cool',the user sees people performing and enjoying music, and aims to grab the user's attention with key pieces of information i.e "Trickle aims to be one of the best music streaming services", "users can access a music player and a large collection of music from great artists". These slides use keys words that were researched and found to have a good balance of being used frequently whilst not having high amounts or organic competition'. 
The user is shown the membership options and the associated costs and is invited to sign up before being presented with a series of short paragraphs that try to explain to the user the great service that is on offer whilst being conscious not to cause the user to lose interest by by having to read too much text. 

![Landing Page]( /media/home_page_two.JPG)

## Sign Up:

Users can sign up by clicking on the 'Sign Up' link at the top of the landing page or by using the sign up buttons on the two cards showing the pricing information. Log in/ Log out is confirmed with a message displayed after each action.

![Sign Up Page]( /media/home_page_two.JPG)

## Log in/ Out:
Once signed up, the user can then log in. Feed back is provided to the user informing them they have successfully signed in. The user is then immediately presented with membership options with links to subscribe. The music content is 'hidden' unitl a membership has been purchased.
![Sign In Page]( /media/sign_in_page.JPG)

Logging out brings the user back to the home page with a message confirming the user has logged out.
![Sign Out Page]( /media/log_out_page.JPG) 

## Navigation Bar:
The navigation bar consists of a 'Home', ' Sign Up' and 'Login' link prior to logging in. However, once logged in, the user now has access to 2 more links, 'Playlists', and 'Profile'. Super users have access to a 'Add music' page where music can be uploaded without having to access the admin page.
For medium screens and smaller, the navigation bar changes to a mobile-friendly drop down menu containing all of the links.

## Logo
The top left of the page is home to a nice custom Trickle logo that I made at Vectr.com. Its a water drop with a musical note and was inspired by 'streaming' music. Like wise the banner is 'digital' water, again keeping with the theme of 'streaming'. Maybe one day, 'trickling' will become a verb much like googling...

## Logged in Status
On the top right, just under the nav bar is one line, highlighted in yellow, which clearly displays to the user that they are logged in. This also turned out to be very handy for me during testing so I could see which account I was currently using.

## Footer:
The footer  contains a link to britannica.com where the user can learn about why people like music. Britanica is a trust worthy source for information. There is also a link to the Trickle facebook page and  a simple copyright message against a dark grey background. There is also a news letter sign up input field on the bottom right corner of the footer for subscribing to news letters.
![Footer]( /media/footer.JPG)

## Home :
Here the user can browse all of the music content on offer. Each song is presented individually in a card like format. Each card shows the track title and artist name along side some cover art. Clicking on the cover brings the user to the music player page where the track can be listened to.
![Home Page]( /media/home_page.JPG)

## Search Bar
At the top in the center of the page is a search bar where the user can type in any key word or a few letters and matching track or artists will be returned allowing for the user to be able to find music without having to search through page after page. If no results are found following a search, the user is presented with a short message asking them to try another search term. There is also a 'cancel' button that can be used to bring the user back to the home page and is a simple way to refresh the search results so that the user doesnt have to use the nav bar or back button.

## Add to Playlist Button
On each card is an 'add to playlist button'. Clicking this button brings the user to a page where they can select a playlist to add the track to.

## Paginator
At the bottom of the page is a paginator, which currently limits the numer of songs displayed on a page to 15. I chose an odd number be it seems like a reasonable amount of content on one screen and not overwhelming for the user.

## Music Player:
A core component of the application is the music player. Here, the user can listen to music, for now , the next or previous buttons dont do anything at present (this will be fixed in the future) , though the play/ pause button works as expected and the volume can be adjusted using the volume slider. The volume can be muted by pressing the speaker icon and the propgress bar can be used to seek. The artist name, track title and cover art are displayed on the music player.
![Music Player]( /media/music_player.JPG)

## Playlists:
On the playlists page, the user can create playlists by pressing the "Add playlist" button. The user is then brought to another page where they can name their new playlist and click save to create the playlist. The user is then redirected to the Playlists page where all of their playlists are listed. 

Each play list has two buttons, one for editing the playlist name, and one for deleting the playlist. Pressing the delete button brings the user to a confirmation page where a warning message is displayed advising that the deletion will be permanent. This helps the user avoid accidental deletion.  The delete page has a large red button too so that its clear to teh user to beware.  To open the playlist, the user must click on the playlist name.
Once inside the playlist, all of the songs added to the playlist will be listed. Each song can then be listened to be clicking on the cover art.

![Playlists]( /media/playlists.JPG)

## Profile Page:
There is a very basic profile page available to the user. For now, it shows the user the date and time they signed up, subcsribed and when their subscription is due to expire.

![Profile Page]( /media/profile_page.JPG)

## Add Music Page:
Super Users have access to the 'Add Music' page where a simple form is used to upload music files and images to the database.

![Add Musi Page]( /media/add_music_page.JPG)

## Subscribe Page:
When a user first signs up to Trickle.com, they are redirected to the home page where they are presented with membership options, 3 months for 8 euro and 12 months for 20 euro. Each option has its own button which brings the user through to the check out page. The check out page can also be accessed by pressing the 'Subscribe' link in the nav bar. The 'Subscribe link is only visible to users who have signed up but not yet subscribed. 
Here the user will be presented with a message stating the membership option they have selected and how much they will be charged.
Below is a Stripe payment form that can be used to input credit card details etc. When the payment form is submitted, a loading screen appears.

Once payment is processed, a success page loads informing the user with a button conveniently placed to bring the user to the music they paid for.

![Subscribe Page]( /media/payment_success.JPG)

## Features Left To Implement:
* Shuffle/ Random Play feature
* Up next feature
* Add album model to add albums to catalogue 
* Auto suggestions to introduce users to new music
* Imporve profile page to include order numbers
* Add upgrade option to subscription
* Add automatic monthly subscription payment option
* Log of music listened to to provide stats to admin
* More styling and 'polishing' of apps elements

## Testing:
* All links were tested.
* All pages were viewed on all screen sizes.
* Edit/ Delete buttons tested on playlists.
* Test stripe payment form to confirm payment succeeded and webhooks and signals working. 
* Test loading page works.
* Test newsletter sign up form works.
* Test all links work and open in new tab.
* Test pagination and search function work correctly
* Test that message is displayed if playlist is empty.
* Tested all CRUD functionality working correctly.
* Tested music plays.
* Tested music player buttons.
* Tested search and cancel search buttosn work correctly.
* Tested user name is diplayed when logged in.
* Tested users can only access paid content after subscribing.
* Tested only admin can access 'Add music page.
* Tested 'subscription' page is only accessible to users who have no subscription.
* Tested that other users cannot access another users playlists.
* Tested all template if statements are working correctly.
* Checked that data updates correclty when edited.
* Checked that data from database is rendered correctly.
* Checked that form data validation works correctly by attempting to pass strings into integer fields.

## Wireframes:
Below are the wireframes used to conceptualise Trickle. I chose to display the music content on the home page in a list like format for easy browsing. Initially I had planed to list the music in one column, but settled for three columns on a full sized screen as I felt this would provide enough choice to the user without overwhelming them with too many options.
![Wire Frame 1]( /media/wireframe_one.JPG)
![Wire Frame 2]( /media/wireframe_two.JPG)

## Database Schema:
Below is the schema for the database used in Trickle. There are 6 models in total.
![Database schema]( /media/models.JPG)

## Epics & User Stories:
The goal in develpoing Trickle was to create an app that allows the user to have access to a good music player, with a large selection of music in a modern format for an affordable price. Rather that try and cater for all tatses of music, I decide to focus primary on one genre i.e rap music given its mass appeal and demand for new sounds and styles
* As a user, I can log in /out so I can access music and protect my account when I'm not using the app.
* As a user I can register so that I can access the sites content.
* As a user, I can recover password so that I can access my account if I forget my password.
* As a user I can browse music so I can see all the music on offer.
* As a user, I can select music to play so I can listen to music.
* As a user, I can use a music player so that I can play/pause/skip a song.
* As a User, I can subscribe to the service so that I can access all content.
* As a user, I can randomly select music so that I can select music to play when I'm unsure of what to listen to.
* As a user, I can see what song is next up in playlist or random playlist so I can see what song will play next.
![User Stories]( /media/user_stories.JPG)

## Solved Bugs:
1. I had difficulty in preventing users from beign able to see eachothers playlists, though I was able to over come this by usign foreign keys to the usr profile.

## Remaining Bugs:
* Users are able to see other users playlists from the playlist form and can add songs to those playlists though they cannot see, edit or delete other users playlists.
* Both 8 euro and 20 euro subscriptions only provide 90 days access instead of 90 or 365 days respectively. 
* Cannot get the payment intent  to print to console.
* previous an dnext buttons on music player not wired up.

## Validator Testing:
* Code for all pages was passed through the W3 Markup validator which deteced errors related to template variables which if handnt encountered before. I chose to ignore these errors as teh code is PEP8 compliant and works.
* Javascript code was passed through the JShint validator. While several warnings were detected, the javascript code works fine.
* PEP8 validator was used within the gitpod workspaces and found no Python problems.

## Deployement:
I deployed the Sentry log app by doing the following:
1. Create Heroku App.
2. Attached the database.
3. Prepared environment and settings.py files.

Then I set up static and media files that are stored on Cloudinary:
1. Go to heroku
2. got to config vars and add a key 'DISABLE_COLLECTSTATIC' and input a value of 1.
3. sign up to cloudinary
4. copy cloudinary API environment variable.
5. In envy.py file add os.environ["CLOUDINARY_URL"] = "past cloudinary API environment variable here". Ensure you delete 'CLOUDINARY_URL='.
6. Go to heroku dashboard > config vars  add a new key 'CLOUDINARY_URL' with the value same as the cloudinary API environment variable.
7. Add new key DISABLE_COLLECTSTATIC and add a value of 1.
8. Go to settings.py > INSTALLED_APPS and add'cloudinary'.
9. go to end of settings page and add ' STATICFILES_STORAGE = 'cloudinary_storage.StaticHashedCloudinaryStorage'
10. STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
11. On the line below ass 'os.path.join(BASE_DIR, 'staticfiles')
12. Add on rthe line below MEDIA_URL = '/media/'
13. On teh line below add, DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
14. Under BASEDIR add TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
15. Go to templates and add [TEMPLATES_DIR] as the valuef or 'DIRS'
16. Go to ALLOWED_HOSTS and add 'sentry-log.herokuapp.com', 'localhost' into the square brakets.
17. create 3 folders in the top directory, static, media and templates.
18. Create profile.
19. Inside procfile type 'web: gunicorn codestar.wsgi'
20. Save, add , commit (deployement commit) and push files to github.
21. Go to heroku dash board > deploy and click github for deployment method.
22. Search for repo.
23. Click connect beside your app.
24. Click 'deploy branch'.
25. When aHeroku states that app has been deployed successfully, click on 'open app' to view the app.
26. Set DEBUG to False.
27. Type "'X_FRAME_OPTIONS = 'SAMEORIGIN'"
28. Save, add , commit and push to repo.
29. Go to Herok > config vars and delete DISABLE_COLLECTSTATIC.
30. Click 'Deploy'
31. Scroll to end of page and click, 'deploy branch'.
32. Click Open app.

## Credits:
* Onojakpor Ochuko - His tutorial helped me code a music player that I used in my app. His tutorial can be found here: https://www.section.io/engineering-education/how-to-build-a-music-player-using-django/
* Full Width Pics v5.0.5 template from Startbootstrap which can be found here: https://startbootstrap.com/template/full-width-pics
* My mentor Gurjot Singh for pointing me in the right direction for implementing a music player.
* W3Schools.com for quick refreshers.
* Bootstrap doc for loads of useful inforation and handy components, especially the code for pagination which can be foudn here https://getbootstrap.com/docs/5.0/getting-started/introduction/
* stackoverflow for information on various error codes.
* Code intitute for the great learning content.

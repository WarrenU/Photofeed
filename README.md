Steps to setup project on your machine:
```
git clone https://github.com/WarrenU/photofeed.git
cd photofeed
pip install virtualenv
virtualenv env
source env/bin/activate
chmod +x ./setup.sh
_ ./setup.sh
deactivate
```

### Comments App:
1. Model that allows for Photographers to make Comment(s) on Photo(s).
3. ModelViewSet allows for Create, Read, Update, Delete

### Photographers App:
Serves as link to django's user model, by having OneToOne w/ User. Useful
for showing who authored a photo or comment. Also a point of interest for
following other users. A Photographer has a location, so we are matching 
Photographer's locations to locations of Photo objects, in our feed endpoint.
1. ModelViewSet allows for Create, Read, Update, Delete
2. PhotographerSerializer overrides create and update to handle User &
 Photographer editing.
3. To see a photographer's Feed of photos near their location & of
 photographers they are following, visit: `/photographers/1/feed/`
4. To follow a user, you could update Photographer,
 Do a post request to: `photographers/1/follow` where the id in the url is who
 you (logged in user) wants to follow.

### Photos App:
Photos are uploaded by a Photographer, and are taken at a certain location.
Provide a string to identify a location of where the Photo was. (Orange, 
Newport Beach, Irvine) for example.
1. ModelViewSet allows for Create, Read, Update, Delete
2. List view of comments is available: `/photos/1/comments/`,
 we are querying a list of Comment objects, related to Photo id 1,
 as per example with link: `/photos/1/comments/`
# Product Backlog

- [ ] #1: Account management for users
- [ ] #2: Urls management for users
- [ ] #3: Type of urls
  - [ ] #4: Short urls
  - [ ] #5: userspace urls
  - [ ] #6: Custom urls
  - [ ] #7: ephimeral urls, once clicked the url is deleted
- [ ] #4: Urls analytics
- [ ] #5: UI theme
  - [ ] #6: dark mode
  - [ ] #7: light mode
  - [ ] #8: equity features

- [ ] User profile
  - [ ] name
  - [ ] bio
  - [ ] pronouns
  - [ ] demographics
  - [ ] avatar or profile picture
  - [ ] links
    - [ ] twitter
    - [ ] instagram
    - [ ] github
    - [ ] linkedin
    - [ ] facebook
    - [ ] youtube
    - [ ] twitch
    - [ ] tiktok
    - [ ] snapchat
    - [ ] reddit
    - [ ] discord
    - [ ] telegram
    - [ ] whatsapp
    - [ ] email
    - [ ] phone
    - [ ] website
    - [ ] custom
- [ ] User settings
  - [ ] theme
  - [ ] language
  - [ ] timezone
  - [ ] currency
  - [ ] notifications
  - [ ] privacy
  - [ ] security
  - [ ] billing
  - [ ] account
  - [ ] support
  - [ ] legal
  - [ ] custom
- [ ] Redirections
  - [ ] when visit tify.one redirect to app.tify.one

- [] #1: As a user, I want to be able to create a new account
- [] #2: As a user, I want to be able to login
- [] #3: As a user, I want to be able to logout
- [] #4: As a user, I want to be able to create a new url
- [] #5: As a user, I want to be able to see my urls
- [] #6: As a user, I want to be able to see my url details
- [] #7: As a user, I want to be able to update my url
- [] #8: As a user, I want to be able to delete my url

- [ ] implement images: `pip install pillow` to handle images
- [ ] in the template, add a form to upload an image
- [ ] `<form enctype="multiple/form-data' method='POST'>`
- [ ] in the view, add a method to handle the image using `request.FILES`
- [ ] in the model, add a field to store the image

## Sprint Backlog

### user stories

- [ ] as a user i want to be able to creat a short url
- [ ] as a user i want to be able to see the short url
- [ ] as a user i want to be able to see the long url
- [ ] as a user i want to be able to see the number of clicks
- [ ] as a user i want to be able to see the date of creation
- [ ] as a user i want to be able to see the date of last click
- [ ] as a user i want to be able to see the date of last update
- [ ] as a user i want to be able to see the date of expiration

- [ ] as a user i want to be able to manage my profile

## tasks

- [ ] create a model for the url
- [ ] create a mutation for the url
- [ ] create a query for the url
- [ ] create a view for the url
- [ ] create a template for the url
- [ ] create a form for the url
- [ ] create a serializer for the url
- [ ] create a model for the url

## Sprints

### Sprint 1

- MVP
  - Create a short url, see urls, see details, update and delete urls
  - Redirect to the long url using the hash
  - style forms using bootstrap and render using django-widget-tweaks
  - basic menu and layout
  - CRUD operations
  - Opengraph redirection

#### user stories sprint 1

- [x] as a user i want to be able to creat a short url
- [x] as a user i want to be able to use CRUD operations on my urls

### Sprint 2

- [ ] implement user authentication
- [ ] apply authentication to views

#### user stories sprint 2

- [ ] as a user i want to be able to signup and signin

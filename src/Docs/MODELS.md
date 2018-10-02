Model Architecture planning

Membership
    -slug 
    -type (free, pro, enterprise)
    -price
    -stripe plan id

UserMembership
    -user                       (foreign key to default user)
    -stripe customer id
    -membership type            (foreign key to Membership)

Subscription
    -user membership            (foreign key to userMembership)
    -stripe subscription id     
    -active

Course
    -slug
    -title
    -description
    -allowed memberships        (foreign key to Membership)


lesson
    -slug
    -title
    -course                     (foreign key to Course)
    -position
    -video
    -thumbnail
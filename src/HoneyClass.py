from DetectClass import DetectClass

# We use HoneySpawnClass as the forwarding destination for all suspicious
# emails. 
# We create a class which accepts an email body 

class HoneySpawnClass:
    def __init_(self, email_id, instance_id):
        self.email_id = email_id
        self.instance_id = instance_id

    def generateEmailIDs(names):
        """
            method generateEmailIDs(List) accepts a list of names separated by
            a space.
        """
        emails = []
        EMAIL_DOMAIN = "@ucdavis.edu"
        for name in names:
            # UC Davis uses the format stated below for emails.
            # If the person's name is John Doe, his email address will be:
            #           jdoe@ucdavis.edu
            #
            # If jdoe@ucdavis.edu is taken, then we arrive at the following
            # scenario:
            # The person's name is Jane Doe, we will resolve this conflict by:
            #           jadoe@ucdavis.edu
            email.append
    def setPhantomEmailID():
        return 

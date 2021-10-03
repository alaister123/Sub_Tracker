from Subscription import Subscription

sub = Subscription()

sub.add_subscription("Youtube",3)
sub.add_subscription("FB",3)
sub.add_subscription("Netflix",3)
sub.remove_subscription("Youtube")
sub.display()
sub.save("test.txt")

subnew = Subscription()
subnew.load('test.txt')
subnew.display()
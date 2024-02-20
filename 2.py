a = int(input("第一队的实力"));
b = int(input("第二队的实力"));
c = int(input("第三队的实力"));
d = int(input("第四队的实力"));
avb = int(a > b)*3 + int(a == b);
avc = int(a > c)*3 + int(a == c);
avd = int(a > d)*3 + int(a == d);
score = avb + avc +avd;
print("总分为%d"%(score));

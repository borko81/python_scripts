# Mask to prefix

def mask_to_prefix(mask):
    mask = '255.255.255.224'
    conv_mask = [bin(int(i))[2:] for i in mask.split('.')]
    prefix = sum([x.count('1') for x in conv_mask])
    print(prefix)

# Prefix to mask

def prefix_to_mask(prefix):
    mask = '1'*prefix
    mask = [_ for _ in "".join(reversed(mask.zfill(32)))]
    for _, c in enumerate(mask):
        if _ in [8, 16, 24]:
            mask[_] = '.' + c
        else:
            mask[_] = c
    print(".".join([str(int(x, 2)) for x in "".join(mask).split('.')]))


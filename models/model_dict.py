from models.segment_anything.build_sam import sam_model_registry
from models.segment_anything_samus.build_sam_us import samus_model_registry

def get_model(modelname="SAM", args=None, opt=None):
    if modelname == "SAM":
        model = sam_model_registry['vit_b'](args = args, checkpoint=args.sam_ckpt)
    elif modelname == "SAMUS":
        model = samus_model_registry['vit_b'](args=args, checkpoint=args.sam_ckpt)
    elif modelname == "SAMUS_noCNN":
        model = samus_model_registry['vit_b_no_refine'](args=args, checkpoint=args.sam_ckpt)
    elif modelname == "APSAM":
        model = samus_model_registry['vit_b_apsam'](args=args, checkpoint=args.sam_ckpt)
    else:
        raise RuntimeError("Could not find the model:", modelname)
    return model

from utils import io as utils_io
import os

# config_dict = utils_io.loadModule("./configs/config_train_encodeDecode_pose.py").config_dict
config_dict = utils_io.loadModule("./configs/config_train_encodeDecode.py").config_dict
config_dict['num_workers'] = 0
config_dict['label_types_test'].remove('img_crop')
config_dict['label_types_train'].remove('img_crop')
config_dict['batch_size_train'] = 1
config_dict['batch_size_test'] = 1

config_dict['n_hidden_to3Dpose'] = 2

# ------------------
# From config_train_encodeDecode_pose
config_dict['label_types_test']  += ['pose_mean','pose_std']
config_dict['label_types_train'] += ['pose_mean','pose_std']
config_dict['latent_dropout'] = 0

config_dict['shuffle_fg'] = False
config_dict['shuffle_3d'] = False

config_dict['train_scale_normalized'] = 'mean_std'
# ------------------


if 0:
    # NVS VAE, smaller latent space of 100*3 3D and 64 FG, 150k KL annealing, 0.001 KL 3D and 0.0001 KL FG weights, with HUE data augmentation
    network_path = './output/trainNVS_wRGB1_wImgNet2_wKL3d0o001_wKLfg1e-05_KLa150000_skipBG0_3d300_fg64_3dTrue_shuffleFGTrue_shuffle3dTrue_h36m_lr0o001_vaeFGTrue_vae3dTrue_hueTrue_'
    config_dict['network_path'] = network_path
    config_dict['pretrained_network_path'] = network_path + '/models/network_best_val_t1.pth'
    config_dict['latent_fg'] = 64
    config_dict['latent_3d'] = 100*3
    config_dict['variational_fg'] = True
    config_dict['variational_3d'] = True
    config_dict['variational'] = True

# Report: beta-VAE
if 1:
    # NVS VAE, smaller latent space of 100*3 3D and 64 FG, KL annealing, 0.001 KL 3D and 0.0001 KL FG weights
    network_path = './output/trainNVS_wRGB1_wImgNet2_wKL3d0o001_wKLfg1e-05_KLa100000_skipBG0_3d300_fg64_3dTrue_shuffleFGTrue_shuffle3dTrue_h36m_lr0o001_vaeFGTrue_vae3dTrue_'
    config_dict['network_path'] = network_path
    config_dict['pretrained_network_path'] = network_path + '/models/network_best_val_t1.pth'
    config_dict['latent_fg'] = 64
    config_dict['latent_3d'] = 100*3
    config_dict['variational_fg'] = True
    config_dict['variational_3d'] = True
    config_dict['variational'] = True

if 0:
    # NVS VAE, smaller latent space of 100*3 3D and 64 FG, KL annealing, 0.001 weight for both
    network_path = './output/trainNVS_wRGB1_wImgNet2_wKL3d0o001_wKLfg0o001_KLa100000_skipBG0_3d300_fg64_3dTrue_shuffleFGTrue_shuffle3dTrue_h36m_lr0o001_vaeFGTrue_vae3dTrue_'
    config_dict['network_path'] = network_path
    config_dict['pretrained_network_path'] = network_path + '/models/network_best_val_t1.pth'
    config_dict['latent_fg'] = 64
    config_dict['latent_3d'] = 100*3
    config_dict['variational_fg'] = True
    config_dict['variational_3d'] = True
    config_dict['variational'] = True

# Report: AE
if 0:
    # Deterministic AE, smaller latent space of 100*3 3D and 64 FG
    network_path = './output/trainNVS_wRGB1_wImgNet2_wKL3d0o001_wKLfg0o001_KLa0_skipBG0_3d300_fg64_3dTrue_shuffleFGTrue_shuffle3dTrue_h36m_lr0o001_vaeFGFalse_vae3dFalse_'
    config_dict['network_path'] = network_path
    config_dict['pretrained_network_path'] = network_path + '/models/network_best_val_t1.pth'
    config_dict['latent_fg'] = 64
    config_dict['latent_3d'] = 100*3
    config_dict['variational_fg'] = False
    config_dict['variational_3d'] = False
    config_dict['variational'] = False

# Report: VAE with weights 1
if 0:
    network_path = './output/trainNVS_wRGB1_wImgNet2_wKL3d1_wKLfg1_KLa0_skipBG0_3d300_fg64_3dTrue_shuffleFGTrue_shuffle3dTrue_h36m_lr0o001_vaeFGTrue_vae3dTrue_hueFalse_'
    config_dict['network_path'] = network_path
    config_dict['pretrained_network_path'] = network_path + '/models/network_best_val_t1.pth'
    config_dict['latent_fg'] = 64
    config_dict['latent_3d'] = 100*3
    config_dict['variational_fg'] = True
    config_dict['variational_3d'] = True
    config_dict['variational'] = True

if 0:
    # Normal VAE without rotation
    network_path = './output/trainNVS_wRGB1_wImgNet2_wKL3d0o01_wKLfg0o01_KLa100000_skipBG0_3d600_fg128_3dTrue_shuffleFGFalse_shuffle3dFalse_h36m_lr0o001_vaeFGTrue_vae3dTrue_'
    config_dict['network_path'] = network_path
    config_dict['pretrained_network_path'] = network_path + '/models/network_best_val_t1.pth'
    config_dict['shuffle_fg'] = False
    config_dict['shuffle_3d'] = False
    config_dict['latent_fg'] = 128
    config_dict['latent_3d'] = 200*3
    config_dict['variational_fg'] = True
    config_dict['variational_3d'] = True
    config_dict['variational'] = True

if 0:
    network_path = './examples'
    config_dict['pretrained_network_path'] = network_path + '/network_best_val_t1.pth'
    if not os.path.exists(config_dict['pretrained_network_path']):
        import urllib.request
        print("Downloading pre-trained weights, can take a while...")
        urllib.request.urlretrieve("http://documents.epfl.ch/groups/c/cv/cvlab-unit/www/data/ECCV2018Rhodin/network_best_val_t1.pth",
                                   config_dict['pretrained_network_path'])
        print("Downloading done.")

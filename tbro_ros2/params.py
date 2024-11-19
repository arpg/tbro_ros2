import os


class Parameters:
    def __init__(self):

        # Root directory in which the ColoRadar Bags are stored
        # self.directory = '/media/giantdrive/andrew/ColoRadar/resampled/'
        self.directory = "/media/harel/Data/coloradar"
        # self.directory = '/home/kharlow/andrew/velocity_resampled/'
        # self.directory = '/home/arpg/datasets/andrew/resampled/'
        # self.directory = '/home/arpg/datasets/bags/'
        # Text file containing bag file names
        self.list_bags = "test_bag_list.txt"
        # Radar topic, type dca1000_device/RadarCubeMsg
        self.topic_radar = "/cascade/heatmap"
        # Odometry Topic used to align heatmaps, type nav_msgs/Odometry
        self.topic_odom = "/lidar_ground_truth"
        self.topic_imu = "/gx5/imu/data"
        # File containing odom to radar transform
        self.tf_base_to_radar = "calib/transforms/base_to_cascade.txt"
        self.tf_base_to_imu = "calib/transforms/base_to_imu.txt"
        # File containing pre-trained encoder weights
        # self.pretrained_enc_path = '/home/arpg/results_training/results/best_encoder_modified.model'
        # self.pretrained_enc_path = '/home/kharlow/ws/TBRO/src/TBRO/scripts/models/weights/best_encoder_modified.model'
        # self.pretrained_enc_path = '/home/arpg/results_training/second_motion_only_epoch_50_batch_10_lr_1e-05_tbro_test_batch.model'
        # self.pretrained_enc_path = '/home/arpg/custom_ratio_motion_test_epoch_50_batch_10_lr_1e-05_tbro_test_batch.model'
        #         # self.pretrained_enc_path = '/home/arpg/new_kernel_test_epoch_25_batch_10_lr_1e-05_pretrained_tbro_test_batch.model'

        #         self.pretrained_enc_path = None
        # self.pretrained_enc_path = '/home/kharlow/new_kernel_test_encoder.model'
        # self.pretrained_enc_path = '/home/arpg/new_kernel_test_epoch_25_batch_10_lr_1e-05_pretrained_tbro_test_batch.model'

        self.pretrained_radar_enc_path = (
            "/media/harel/Data/coloradar/only_motion_encoder.model"
        )
        self.pretrained_imu_enc_path = (
            "/media/harel/Data/coloradar/bidirectional_pred_model.pth"
        )

        self.forward_seq_only = True

        # Max sequence length (optional) (int or None for full sequence)
        # self.max_length = 8
        # self.batch_size = 2
        # self.epochs = 25

        self.max_length = 200
        self.batch_size = 64
        self.epochs = 100

        # Values for data conversion
        # self.max_length = 1
        # self.batch_size = 1
        # self.epochs = 1

        self.radar_shape = [64, 128, 64]
        self.mean_enable = True
        self.hidden_size = 1024

        self.imu_length = 200

        # self.learning_rate = 1.0e-7
        self.learning_rate = 1.0e-3
        # self.learning_rate = 4.0e-3

        self.alphas = [1.0, 1.0]
        self.betas = [1.0, 1.0]
        self.gammas = [1.0, 1.0]

        # Text file with filesnames from which to load training data
        # self.train_files = 'train_dataset.txt'
        self.train_files = "random_train_dataset.txt"
        # self.train_files = 'random_train_dataset.txt'

        # Text file with filenames from which to load validation data
        self.val_files = "random_test_dataset.txt"
        # File in which to save the model weight
        # self.save_filename = 'new_kernel_full_'+str(self.epochs)+'_batch_'+str(self.batch_size)+'_lr_'+str(self.learning_rate)+'_test_batch.model'
        # self.save_filename = 'no_motion_epoch_'+str(self.epochs)+'_batch_'+str(self.batch_size)+'_lr_'+str(self.learning_rate)+'_test_batch.model'
        # self.save_filename = 'imu_epoch_'+str(self.epochs)+'_batch_'+str(self.batch_size)+'_lr_'+str(self.learning_rate)+'_test_batch.model'
        # File from which to load model for testing only
        self.load_filename = ""
        # Bool, load model and run on test data only without training
        self.eval_only = False

        # TEST VARIABLES:

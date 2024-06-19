% Load the Infrared and Visible images
IR_folder = '/Users/shefalisingh/Desktop/mini_proj/IR/images';
RGB_folder = '/Users/shefalisingh/Desktop/mini_proj/RGB/images';

IR_files = dir(fullfile(IR_folder, '*.jpg'));
RGB_files = dir(fullfile(RGB_folder, '*.jpg'));

% Create folder for storing fused images
output_folder = '/Users/shefalisingh/Desktop/mini_proj/fused_img';
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% Fusion Parameters
lambda = 0.5; % Weight for the fusion, can be adjusted

for i = 1:min(numel(IR_files), numel(RGB_files))
    % Read the images
    IR_image = imread(fullfile(IR_folder, IR_files(i).name));
    RGB_image = imread(fullfile(RGB_folder, RGB_files(i).name));

    % Convert IR image to grayscale if it is not already
    if size(IR_image, 3) == 3
        IR_image = rgb2gray(IR_image);
    end
    
    % Convert images to double format for processing
    IR_double = im2double(IR_image);
    RGB_double = im2double(RGB_image);
    
    % Perform fusion using the FPDE algorithm
    fused_image = fpde_fusion_algorithm(IR_double, RGB_double, lambda);

    % Save the fused image
    [~, filename, ~] = fileparts(IR_files(i).name);
    fused_filename = [filename '_fused.jpg'];
    imwrite(fused_image, fullfile(output_folder, fused_filename));
    
    fprintf('Fused image saved: %s\n', fused_filename);
end

function fused_image = fpde_fusion_algorithm(IR_image, RGB_image, lambda)
    % This function fuses the IR and RGB images using fractional partial differential equation (FPDE).
    % lambda determines the balance between IR intensity and RGB color.

    % Ensure IR_image is single-channel (grayscale)
    if size(IR_image, 3) ~= 1
        error('IR image should be a grayscale image.');
    end
    
    % FPDE Fusion Algorithm Implementation
    % (You can replace this with your FPDE fusion algorithm implementation)

    % Placeholder implementation: Simply take the average of the images
    fused_image = lambda * IR_image + (1 - lambda) * RGB_image;
end

img = imread("input");
[len, high] = size(img);
k = 4;
start_list = 0;
end_list = 0;
img_r=img;
for i = 1:len
    for j = 1:high
        if j >k && j<high-k
            slice = img(i,j-k:j+k);
            start_list = j-k;
            end_list = j+k;
        elseif j< k
            slice = img(i,1:j+k);
            start_list = i;
            end_list = j+k;
        elseif j> high-k
             slice = img(i,j-k:high);
             start_list = j-k;
             end_list = high;
        end
        slice_sorted = sort(slice);
        mid = round(length(slice_sorted)/2);
        img_r(i,start_list:end_list)=slice_sorted(mid); 
    end
end
imwrite(img_r, "output");
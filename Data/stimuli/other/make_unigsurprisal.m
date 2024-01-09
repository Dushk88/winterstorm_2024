clear all
close all
clc
 
 
% load the csv file
files = dir('/*.csv');
load('subtlexall.mat');

subtlex_table=cell2table(subtlex_word_phonems);

for i=1:length(files)

    % Extract the word table
    tt = readtable(strcat(files(i).folder,'/',files(i).name));
    
    % for each word save the cohort entorpy in seperate column
    word_rows = find(strcmp('words',tt.tier));
     
    tt.unig(word_rows)=NaN;
    freq_all = sum(str2double(data{:,2}));
    % do for each word
    for j=1:length(word_rows)
        
        % get the list of words starts with the phoneme
        wordnow = lower(wordnow);
        matching_words_ind = find(strcmp(lower(data.Var1),lower(wordnow)));
        freq_new = str2double(table2array(data(matching_words_ind,2)));
            
        
        if strcmp(wordnow,'friended')||strcmp(wordnow,'chapmans')||strcmp(wordnow,'lazily')...
                ||strcmp(wordnow,'hickories')||strcmp(wordnow,'keelboats')...
                ||strcmp(wordnow,'appleseed')||strcmp(wordnow,'marietta')...
                ||strcmp(wordnow,'muskingum')||strcmp(wordnow,'Mansfield')...
                ||strcmp(wordnow,'pomace')||strcmp(wordnow,'thoreau')...
                ||strcmp(wordnow,'hulled')||strcmp(wordnow,'queerness')...
                ||strcmp(wordnow,'appleseed')||strcmp(wordnow,'steubenville')
            freq_new = 1;
        end

            
        pword = (freq_new)/freq_all;
        tt.unig(word_rows(j)) = -log2(pword);
      
                
    end
       
    disp(sum(isnan(tt.w_freqp)| isinf(tt.w_freqp)))   
    % save as new csv file
    writetable(tt,strcat('/new',files(i).name));  
        

end


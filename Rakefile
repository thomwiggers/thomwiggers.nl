desc 'Running Jekyll with serve -w'
task :dev do
  system('bundle exec compass compile')
  system('bundle exec jekyll serve')
end


# rake write[title,category]
desc "Given a title as an argument, create a new post file"
task :write, [:title, :category] do |t, args|
  filename = "#{Time.now.strftime('%Y-%m-%d')}-#{args.title.gsub(/\s/, '_').downcase}.markdown"
  path = File.join("_posts", filename)
  if File.exist? path; raise RuntimeError.new("Won't clobber #{path}"); end
  File.open(path, 'w') do |file|
    file.write <<-EOS
---
layout: post
category: #{args.category}
title: #{args.title}
date: #{Time.now.strftime('%Y-%m-%d %k:%M:%S %z')}
---
EOS
    end
    puts "Now open #{path} in an editor."
end

# command: rake rsync:dryrun or rake rsync:deploy
namespace :rsync do
  host = 'clearlyreta.rded.nl:/var/www/thomwiggers.nl'

  desc "--dry-run rsync"
    task :dryrun do
      puts "DRY RUN!"
      system('rm -f .well-known/thomwiggers.asc')
      system('gpg --output .well-known/thomwiggers.asc --armor --export 915D4ED34871E82F')
      system('bundle exec jekyll clean')
      system('bundle exec compass compile')
      system('bundle exec jekyll build --lsi')
      system("rsync _site/ -ave ssh --dry-run --delete #{host}")
    end
  desc "rsync"
    task :deploy do
      system('rm -f .well-known/thomwiggers.asc')
      system('gpg --output .well-known/thomwiggers.asc --armor --export 915D4ED34871E82F')
      system('bundle exec jekyll clean')
      system('bundle exec compass compile')
      system('bundle exec jekyll build --lsi')
      system("rsync _site/ -ave ssh --delete #{host}")
    end
end

